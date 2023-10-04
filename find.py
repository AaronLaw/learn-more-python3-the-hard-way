# A implementation of `find` in Python as cli

from typing import Union, Any, Optional
from Command import Find

import click

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-name', '--filename', help='')
@click.option('-type', '--type', help='')
def find(path: click.Path, filename: str, type: str) -> None:
    """Print matching files.
    """
    Find(path, filename, type).execute()

if __name__=="__main__":
    find()