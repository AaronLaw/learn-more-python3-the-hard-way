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

@click.command()
@click.argument('filenames', nargs=-1, type=click.Path(exists=True))
@click.option('-n', '--numbers', is_flag=True, help='Print line numbers')
def cat(filenames, numbers):
    """Print and concatnate files.
    """
    for filename in filenames:
        with open(filename, 'r') as file:
            if numbers:
                lines = file.readlines()
                for i, line in enumerate(lines, start=1):
                    click.echo(f"{i}\t {line}", nl=False)
            else:
                contents = file.read()
                click.echo(contents)

if __name__=="__main__":
    cat()