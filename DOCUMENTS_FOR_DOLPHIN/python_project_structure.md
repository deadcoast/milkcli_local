milk-cli/
│
├── main.py                          # Main executable script for the 'milk' CLI application
│
├── triggers/                        # Folder containing individual modules for each trigger command
│   ├── __init__.py                  # Makes 'triggers' a Python package
│   ├── sour.py                      # Module for 'sour' trigger functionality
│   ├── man.py                       # Module for 'man' trigger functionality
│   └── [other_triggers].py          # Other trigger command modules
│
├── variables/                       # Folder containing modules for each variable
│   ├── __init__.py                  # Makes 'variables' a Python package
│   ├── core_commands_list.py        # Module for handling '~mom', '~list'
│   ├── help_this_trigger.py         # Module for handling '~h', '~help'
│   ├── path_me.py                   # Module for handling '~?', '~path'
│   ├── milk_nav_back.py             # Module for handling '~back'
│ 	└── [other_commands].py 		 # other variable commands 
│
├── adders/                          # Folder for handling '+' operation to add new triggers or variables
│   ├── __init__.py                  # Makes 'adders' a Python package
│   └── add_command.py               # Module for handling '+' operation
│
├── utilities/                       # Folder for shared utility functions, if necessary
│   ├── __init__.py**currently voided# Makes 'utilities' a Python package
│   └── helpers.py          		 # Utility modules
│
├── milk_cli.log                     # Log file capturing CLI activity and errors
│
└── README.md                        # Documentation explaining how to use the 'milk' CLI

