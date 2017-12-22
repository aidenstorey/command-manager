import importlib
import os


def discover_commands(base_path, *sub_paths):
    commands_dir = os.path.join(base_path, 'commands', *sub_paths)
    for item in os.listdir(commands_dir):
        path = os.path.join(commands_dir, item)
        if os.path.isfile(path):
            try:
                importlib.import_module('.'.join(['commands', *sub_paths, item]))
            except ImportError:
                pass
        elif os.path.isdir(path) and '__pycache__' not in path:
            discover_commands(base_path, *sub_paths, item)
