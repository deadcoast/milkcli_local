# This would likely be part of a larger utility module.

# This would likely be part of a larger utility module.

class CLINavigator:
    def __init__(self):
        self.history = []

    def back(self):
        if self.history:
            return self.history.pop()
        else:
            print("No previous state to return to.")

# An instance of CLINavigator would need to be accessible by the command modules to use `back`.