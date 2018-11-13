import click

from utils.logging_config import configure_logging

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
APP_NAME = 'ZIP Shotgun'
VERSION = '1.0.0'


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=VERSION, prog_name=APP_NAME)
def zip_shotgun():
    pass


if __name__ == '__main__':
    configure_logging()
    zip_shotgun()
