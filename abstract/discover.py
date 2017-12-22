import importlib
import os


def discover_commands(base_path):
    commands_dir = f'{base_path}/commands/'
    for file in os.listdir(commands_dir):
        path = os.path.join(commands_dir, file)
        if os.path.isfile(path):
            try:
                importlib.import_module(f'commands.{file.split(".")[0]}')
            except ImportError:
                pass
