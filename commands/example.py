import abstract


class Command(abstract.BaseCommand):
  help = 'An example command to show how to create a command'

  def add_arguments(self, argument_parser):
    """Optional method to handle adding arguments to the command line parser.

    @argument_parser: An argparse parser object, see documentation for usage https://docs.python.org/3/library/argparse.html
    """
    argument_parser.add_argument('--test', dest='test', type=int, required=False)

  def handle(self, test):
    """Required method to handle the functionality of the command.

    Arguments for the method map to arguments added to the parser in the `add_arguments` function.
    """
    if test is None:
      raise abstract.CommandException('For best results, passing an integer using `--test <int>` is recommended.')  # Use CommandException for formatted console output.

    print(f'Your integer was: {test}')
