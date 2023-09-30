# Here we use `sys.argv` to get argument from stdin
import sys
from typing import List

def with_argv():
    args: List = sys.argv
    print(args)
    print(f'The file itself is: {args[0]}')


# Here we use `argparse` to get argument from stdin
import argparse

def with_argparse():
    parser = argparse.ArgumentParser(description="To sum up 2 numbers")
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("first", help="The first number",
                        type=int)
    parser.add_argument("second", help="The second number",
                        type=int)

    args = parser.parse_args()
    if args.verbose:
        print(f"this is from args: {args.first} + {args.second}")
    print(args.first + args.second)

# Here we use `click` to get argument from stdin
# click uses decorator to wrap function to a Command <- Python Command Line Tools by Noah Gift 
import click

@click.command()
# @click.option("--add", help="add 2 numbers.")
@click.option("-v", "--verbose", is_flag=True, help="increase output verbosity")
@click.argument("first", type=click.INT)
@click.argument("second", type=click.INT)
def add(first, second, verbose=False):
    if verbose:
        click.echo(f"this is from args: {first} + {second}.")
    click.echo(first + second)


if __name__=="__main__":
    # with_argv()
    # with_argparse()
    add()