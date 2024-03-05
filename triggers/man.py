# File: triggers/man.py
"""
The 'man' trigger module for the 'milk' CLI. This module is responsible for adding new triggers or variables.
"""
import os
import args
from colorama import Fore, Style
import logging


def run(man, variables, args):
    if '~help' or '~h' in args:
        # Call the 'run' function of the 'help_this_trigger' variable module
        variables['help_this_trigger'].run()
    elif '~list' or '~mom' in args:
        # Call the 'run' function of the 'core_commands_list' variable module
        variables['core_commands_list'].run()
    # Verify that the command name starts with the '+' sign
    if not args.command_name.startswith('+'):
        raise ValueError("Command name must start with '+'")

    # Remove the '+' to get the actual command name
    actual_name = args.command_name.lstrip('+')
    commands_list = ['sour', 'man']
    print("The following core commands are available:")
    for command in commands_list:
        print(f"- {command}")
    # Prompting adhering to color and format standards specified in the design document
    print(f"{Fore.CYAN}You are about to add a new command or variable.{Style.RESET_ALL}")
    command_type = input(f"{Fore.CYAN}Please specify the type ('trigger' or 'variable'): {Style.RESET_ALL}").strip().lower()

    if command_type not in ['trigger', 'variable']:
        print(f"{Fore.RED}Error: The type must be either 'trigger' or 'variable'.{Style.RESET_ALL}")
        logging.error(f"{command_type} is not a valid type for the man command.")
        return

    if not command_name.startswith('+'):
        print(f"{Fore.RED}Error: Command name must start with '+' character.{Style.RESET_ALL}")
        logging.error("The command name must start with '+'.")
        return
    command_name = command_name.lstrip('+').strip()
    if not command_name:
        print(f"{Fore.RED}Error: Command name cannot be empty after '+'.{Style.RESET_ALL}")
        return
    if not command_name.isalnum():
        print(f"{Fore.RED}Error: Command name cannot contain non-alphanumeric characters.{Style.RESET_ALL}")
        return
    if not command_name.islower():
        print(f"{Fore.RED}Error: Command trigger name must contain all CAPITAL characters.{Style.RESET_ALL}")
        return


    # Choose the correct directory based on the command type
    directory = 'triggers' if command_type == 'trigger' else 'variables'
    file_path = os.path.join(directory, f"{command_name}.py")

    # Check if file already exists to avoid overwriting
    if os.path.isfile(file_path):
        print(f"{Fore.RED}Error: A {command_type} with the name '{command_name}' already exists.{Style.RESET_ALL}")
        return

    # Get the description for the command or variable
    description = input(f"{Fore.CYAN}Enter a description for the '{command_name}':{Style.RESET_ALL} ")

    # Get a description for the new command
    description = input("Enter a description for this command: ")

    # Create and write to the new command file
    with open(filepath, 'w') as f:
        f.write(f"\"\"\"\n{description}\n\"\"\"\n")
        f.write("def run():\n")
        f.write("    # TODO: Implement the command's functionality\n")

    print(f"Command '{actual_name}' created successfully in the {directory} directory.")

    # Confirmation message adhering to the color standards
    print(f"{Fore.GREEN}A new placeholder for {command_type} '{command_name}' has been created.{Style.RESET_ALL}")
    logging.info(f"A placeholder for {command_type} '{command_name}' was successfully created.")