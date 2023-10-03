# A implementation of `cat` in Python

"""
# some functions of `cat`:

## print the contents of a file to stdout
cat file

## concatnate files into an output file
cat file1 file2 file3 > outfile

## append files into an output file
cat file1 file2 file3 >> outfile

## number the output lines
cat -n file
"""
from typing import Union, Any, Optional
from Command import Cat

import click

@click.command()
@click.argument('filenames', nargs=-1, type=click.Path(exists=True))
@click.option('-n', '--numbers', is_flag=True, help='Print line numbers')
def cat(filenames: click.Path, numbers: bool) -> None:
    """Print and concatnate files.
    """
    Cat(filenames, numbers).execute()

if __name__=="__main__":
    cat()