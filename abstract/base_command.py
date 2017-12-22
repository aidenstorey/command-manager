import argparse

import abstract.exceptions as exceptions
import settings

parser = argparse.ArgumentParser(settings.COMMAND_HELP_TEXT)
sub_parser = parser.add_subparsers(dest='command')

registered_commands = {}


class BaseCommandMeta(type):
    def __new__(mcs, name, bases, class_dict):
        required_attributes = {'help', 'handle'}

        missing_attributes = required_attributes - set(class_dict)
        if missing_attributes:
            raise AttributeError(f'Classes that inherit from BaseCommand must include ({",".join(missing_attributes)}) attribute(s)')

        class_object = super().__new__(mcs, name, bases, class_dict)
        if name != 'BaseCommand':
            mcs.__handle_creation(class_object)
        return class_object

    @staticmethod
    def __handle_creation(class_object):
        module_name = class_object.__module__

        if 'commands' not in module_name:
            return

        module_name = module_name.split('.', 1)[1]

        registered_commands[module_name] = class_instance = class_object()
        command_parser = sub_parser.add_parser(module_name, help=class_object.help)

        try:
            class_instance.add_arguments(command_parser)
        except NotImplementedError:
            pass


class BaseCommand(object, metaclass=BaseCommandMeta):
    help = ''

    def add_arguments(self, arguments_parser):
        raise NotImplementedError()

    def handle(self, **options):
        raise NotImplementedError()


def parse_command():
    result = parser.parse_args().__dict__
    try:
        registered_commands[result.pop('command')].handle(**result)
    except exceptions.CommandException as e:
        print(f'\nCommand Error: {str(e)}')
