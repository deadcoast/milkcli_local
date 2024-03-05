import importlib.util
import sys
import os


def load_module(module_name, directory):
    """Dynamically load a module."""
    filepath = os.path.join(directory, f"{module_name}.py")
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
