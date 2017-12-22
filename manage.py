import os

import abstract


abstract.discover_commands(os.path.dirname(os.path.abspath(__file__)))
abstract.parse_command()
