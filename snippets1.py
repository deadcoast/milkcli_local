import subprocess
import os
import sys
import shutil

def set_gptk(key):
    with open("gptk.txt", "w") as f:
        f.write(key)
    print(f"GPT-3 API key saved: {key}")

def set_windows_env(unrestricted):
    policy = "Unrestricted" if unrestricted else "Restricted"
    subprocess.run(["powershell", f"Set-ExecutionPolicy {policy}"], check=True)

def mkdir(path):
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")

def copy_files(src, dest):
    shutil.copytree(src, dest)
    print(f"Copied files from {src} to {dest}")

def milk_prompt():
    while True:
        cmd = input("> ").strip()
        args = cmd.split()[1:]

        if cmd == "~quit":
            break
        elif cmd == "~github":
            print("<Your GitHub command logic here>")
        elif cmd == "~gptk":
            if len(args) < 1:
                print("Usage: ~gptk <key>")
            else:
                key = args[0]
                try:
                    set_gptk(key)
                except Exception as e:
                    print(f"Error setting GPT-3 API key: {e}")
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
        elif cmd == "~cp":
            if len(args) < 2:
                print("Usage: ~cp <src> <dest>")
            else:
                src, dest = args[:2]
                try:
                    copy_files(src, dest)
                    print(f"Copied files from {src} to {dest}")
                except Exception as e:
                    print(f"Error copying files: {e}")
        # Add more commands here
        else:
            print("Unknown command")
            
readline.parse_and_bind("tab: complete")


def display_help():
    print("Available commands:")
    print("  milk: Enable the CLI (default)")
    print("  autocomplete: Toggle auto-completion for user input")
    # Add more commands here as they are implemented
    print("  help: Display this help menu")

def milk_prompt():
    # ... (existing code)
    elif cmd == "help":
        display_help()

def validate_input(cmd):
    valid_commands = ["milk", "autocomplete", "help"]  # Add more commands as they are implemented
    return cmd in valid_commands

def milk_prompt():
    # ... (existing code)
    if not validate_input(cmd):
        print("Invalid command. Type 'help' for a list of available commands.")

def open_file(path):
    if sys.platform == "win32":
        os.startfile(path)
    elif sys.platform == "darwin":
        subprocess.run(["open", path], check=True)
    else:
        subprocess.run(["xdg-open", path], check=True)

def milk_prompt():
    # ... (existing code)
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


def validate_input(cmd, args):
    valid_commands = {
        "milk": 0,
        "autocomplete": 0,
        "help": 0,
        "open": 1  # Add more commands and their argument counts here
    }
    return cmd in valid_commands and len(args) == valid_commands[cmd]

def milk_prompt():
    # ... (existing code)
    if not validate_input(cmd, args):
        print("Invalid command or argument count. Type 'help' for usage instructions.")
        

def set_gptk(key):
    # Save the key somewhere secure, e.g., in a file or environment variable
    with open("gptk.txt", "w") as f:
        f.write(key)
    print(f"GPT-3 API key saved: {key}")

def milk_prompt():
    # ... (existing code)
    elif cmd == "~gptk":
        if len(args) < 1:
            print("Usage: ~gptk <key>")
        else:
            key = args[0]
            try:
                set_gptk(key)
            except Exception as e:
                print(f"Error setting GPT-3 API key: {e}")

def set_windows_env(unrestricted):
    # ... (existing code)
        subprocess.run(["powershell", f"Set-ExecutionPolicy {policy}"], check=True)
    # ...

def milk_prompt():
    # ... (existing code)
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
                
def mkdir(path):
    subprocess.run(["mkdir", path], check=True)
    print(f"Directory created: {path}")
    
def milk_prompt():
    # ... (existing code)
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


