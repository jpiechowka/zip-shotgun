import click

from utils.logging_config import configure_logging

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
APP_NAME = 'ZIP Shotgun'
VERSION = '1.0.0'

HELP_MSG_COUNT_OF_DIRECTORIES = 'Count of how many directories to go back inside the zip file (e.g 3 means that 3 files will be added to the zip: ' \
                                'shell.php, ../shell.php and ../../shell.php where shell.php is the name of the shell you provided or randomly generated value'
HELP_MSG_SHELL_NAME = 'Name of the shell inside the generated zip file (e.g shell.php). If not provided it will be randomly generated'
HELP_MSG_SHELL_FILE = 'A file that contains code for the shell. If this option is not provided basic php shell will be added instead. ' \
                      'If name is provided it will be added to the zip with the provided name or if not provided the name will be randomly generated.'


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=VERSION, prog_name=APP_NAME)
@click.option('-c', '--count-of-directories', show_default=True, default=15, required=False, type=int, help=HELP_MSG_COUNT_OF_DIRECTORIES)
@click.option('-n', '--shell-name', show_default=False, default=None, required=False, type=str, help=HELP_MSG_SHELL_NAME)
@click.option('-f', '--shell-file', show_default=False, default=None, required=False, type=click.File(mode='r'), help=HELP_MSG_SHELL_FILE)
def zip_shotgun():
    pass


if __name__ == '__main__':
    configure_logging()
    zip_shotgun()
