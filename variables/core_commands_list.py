"""
core_commands_list variable: Lists available commands in the current trigger context.
"""

# variables/core_commands_list.py

"""
This module lists all the core commands available in a particular context.
"""

def run():
    # TODO: Implement logic to retrieve the context-specific command list.
    commands_list = ['sour', 'man']  # Placeholder for actual command list.
    print("The following core commands are available:")
    for command in commands_list:
        print(f"- {command}")