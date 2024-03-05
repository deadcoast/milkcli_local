#!/usr/bin/env python
# milk.py - Main executable script for the 'milk' CLI application

import argparse
import logging
import os
import sys
from utilities.helpers import load_module
from colorama import init, Fore, Style
sys.path.append(os.path.join(os.path.dirname(__file__), 'utilities'))
# Initialize colorama for colored output
init(autoreset=True)

# Set up logging with both file and console handlers
logging.basicConfig(
    level=logging.INFO,
    format=f"{Fore.YELLOW}%(asctime)s - %(levelname)s - %(message)s{Style.RESET_ALL}"
    )

# Define paths for triggers and variables directories
TRIGGERS_DIR = os.path.join(os.path.dirname(__file__), "triggers")
VARIABLES_DIR = os.path.join(os.path.dirname(__file__), "variables")

# Create directories if they don't exist
os.makedirs(TRIGGERS_DIR, exist_ok=True)
os.makedirs(VARIABLES_DIR, exist_ok=True)

# Import the load_module function from utilities.helpers
sys.path.append(os.path.join(os.path.dirname(__file__), "utilities"))  # Adds utilities to module search path


class MilkCLI:
    def __init__(self):
        self.triggers = {}  # Loaded command triggers
        self.variables = {}  # Loaded command variables
        self.parser = argparse.ArgumentParser(description='MILK CLI - Dynamically designed command hub.')
        self.subparsers = self.parser.add_subparsers(dest='command', help='Available commands')
        self.load_triggers()
        self.load_variables()

    # Part of the MilkCLI class in milk.py

    def load_triggers(self):
        """Load all trigger modules dynamically from the triggers directory."""
        triggers = {}
        for filename in os.listdir(TRIGGERS_DIR):
            if filename.endswith('.py') and not filename.startswith('__'):
                trigger_name = filename[:-3]
                module = load_module(trigger_name, TRIGGERS_DIR)
                triggers[trigger_name] = module.run  # Make sure the run function is defined in the trigger modules
        return triggers

    def load_variables(self):
        """Load all variable modules dynamically from the variables directory."""
        variables = {}
        for filename in os.listdir(VARIABLES_DIR):
            if filename.endswith('.py') and not filename.startswith('__'):
                variable_name = filename[:-3]
                module = load_module(variable_name, VARIABLES_DIR)
                variables[variable_name] = module.run  # Make sure the run function is defined in the variable modules
        return variables

    def execute(self):
        args = self.parser.parse_args()
        command = args.command
        if command in self.triggers:
            self.triggers[command](args)
        elif command in self.variables:
            self.variables[command](args)
        else:
            self.parser.print_help()


if __name__ == "__main__":
    cli = MilkCLI()
    cli.execute()
