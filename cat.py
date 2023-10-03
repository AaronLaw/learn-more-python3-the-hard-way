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

import click
from typing import Union, Any, Optional

@click.command()
@click.argument('filenames', nargs=-1, type=click.Path(exists=True))
@click.option('-n', '--numbers', is_flag=True, help='Print line numbers')
def cat(filenames: click.Path, numbers: bool) -> None:
    """Print and concatnate files.
    """
    line_number = 1
    for filename in filenames:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if numbers:
                for line in lines:
                    click.echo(f"{line_number}\t {line}", nl=False)
                    line_number += 1
            else:
                click.echo(''.join(lines))

if __name__=="__main__":
    cat()