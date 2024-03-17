import os
import keyboard
import time
import subprocess
import json
import getpass
from colorama import Fore, Style, init  # For colored output
import readline  # For command history and tab completion
readline.parse_and_bind("tab: complete")
from termcolor import colored  # For more advanced color options
import logging

init()  # Initialize colorama

logging.basicConfig(filename="milk_log.txt", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(msg):
    logging.info(msg)
    print(Fore.GREEN + msg + Style.RESET_ALL)

def log_error(msg):
    logging.error(msg)
    print(Fore.RED + msg + Style.RESET_ALL)

# Load saved data if exists
if os.path.exists("milk_data.json"):
    with open("milk_data.json", "r") as f:
        milk_data = json.load(f)
else:
    milk_data = {}

def save_data():
    # Save data to a file so it persists between sessions
    with open("milk_data.json", "w") as f:
        json.dump(milk_data, f)

# Set up password if not already set
if "password" not in milk_data:
    print("Setting up password...")
    password = getpass.getpass()
    milk_data["password"] = password
    save_data()

def run_command(cmd):
    # Run a command in the terminal and return the output as a string
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log_info("Command executed: " + cmd)
        return result.stdout.decode("utf-8")
    except Exception as e:
        log_error("Error executing command: " + cmd + "\n" + str(e))
        return str(e)
    
def autocomplete(cmd):
    # Add more commands here as they are implemented
    if cmd.startswith("~g"):
        return ["~github"]
    if cmd.startswith("~w"):
        return ["~winpath"]
    if cmd.startswith("~p"):
        return ["~setperms 1", "~setperms 0"]
    if cmd.startswith("op"):
        return [f"~open {f}" for f in os.listdir()]
    if cmd.startswith("m"):
        return ["milk"]
        if cmd.startswith("~h"):
        return ["~help"]
    return []

def validate_input(cmd, args):
    valid_commands = {
        "milk": 0,
        "autocomplete": 0,
        "help": 0,
        "open": 1
        "setperms": 1,
        "setperms": 0,
        "wpath": 0,
        "github": 0
        
        # Add more commands and their argument counts here
    }
    return cmd in valid_commands and len(args) == valid_commands[cmd]

def display_help():
    print("Available commands:")
    print("  milk: Enable the CLI (default)")
    print("  autocomplete: Toggle auto-completion for user input")
    # Add more commands here as they are implemented
    print("  help: Display this help menu")
    print("  github: Display the github reference path")
    print("  winpath: Display the Windows path")
    print("  setperms: Set execution permissions")
    print("  ~setperms 1: Set execution permissions to unrestricted")
    print("  ~setperms 0: Set execution permissions to restricted")

def open_file(path):
    if sys.platform == "win32":
        os.startfile(path)
    elif sys.platform == "darwin":
        subprocess.run(["open", path], check=True)
    else:
        subprocess.run(["xdg-open", path], check=True)  

def mkdir(path):
    subprocess.run(["mkdir", path], check=True)
           
def set_gptk(key):
    # Save the key somewhere secure, e.g., in a file or environment variable
    with open("gptk.txt", "w") as f:
        f.write(key)
    print(f"GPT-3 API key saved: {key}")
    return
def set_windows_env(unrestricted):
    # ... (existing code)
        subprocess.run(["powershell", f"Set-ExecutionPolicy {policy}"], check=True)
    
def milk_prompt():
    # Wait for "milk" to be typed
    keyboard.wait("m")
    keyboard.wait("i")
    keyboard.wait("l")
    keyboard.wait("k")
    # Get the command and check if it's valid
    cmd = input()
    if not cmd.startswith("~"):
        log_error("Invalid command: " + cmd)
        print(colored("Invalid command.", "red"))
        return
    if not validate_input(cmd):
        print("Invalid command. Type 'help' for a list of available commands.")
        return
    # Check password
    password_attempt = getpass.getpass()
    if password_attempt != milk_data["password"]:
        log_error("Incorrect password.")
        print(colored("Incorrect password.", "red"))
        return

    # Run the appropriate command
    if cmd == "~github":
        if "github" in milk_data:
            print(Fore.GREEN + colored(milk_data["github"], "green") + Style.RESET_ALL)
        else:
            print("No github reference path set, Set reference now? (y/n)")
            choice = input()
            if choice.lower() == "y":
                path = input("Enter github path: ")
                milk_data["github"] = path
                save_data()
                elif cmd == "open":
        if len(args) < 1:
            print("Usage: open <path>")
        else:
            path = args[0]
            try:
                open_file(path)
                print(f"Opened {path}")
            except Exception as e:
                print(f"Error opening {path}: {e}")
    elif cmd == "~gptk":
        if len(args) < 1:
            print("Usage: ~gptk <key>")
        else:
            key = args[0]
            try:
                set_gptk(key)
            except Exception as e:
                print(f"Error setting GPT-3 API key: {e}")
    elif cmd == "~mkdir":
        if len(args) < 1:
            print("Usage: ~mkdir <path>")
        else:
            path = args[0]
            try:
                mkdir(path)
                print(f"Directory created: {path}")
            except Exception as e:
                print(f"Error creating directory: {e}")                        
    elif cmd == "help":
        display_help()           
    elif cmd == "~wpath":  # Or you can use ~winpath instead
        if len(args) < 1:
            print("Usage: ~wpath <0|1>")
        else:
            unrestricted = args[0] in ("1", "true", "yes")
            try:
                set_windows_env(unrestricted)
                if unrestricted:
                    print("Windows permission set to unrestricted")
                else:
                    print("Windows permission reset to default")
            except Exception as e:
                print(f"Error setting Windows permission: {e}")

# Start the script
print("Milk script started. Press 'milk' to use...")
readline.parse_and_bind("tab: complete")  # Enable tab completion
while True:
    try:
        milk_prompt()
    except KeyboardInterrupt:
        break