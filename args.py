# Here we use `sys.argv` to get argument from stdin
import sys
from typing import List

def with_argv() -> None:
    args: List = sys.argv
    print(args)
    print(f'The file itself is: {args[0]}')


# Here we use `argparse` to get argument from stdin
import argparse

def with_argparse() -> None:
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
@click.argument('numbers', type=int, nargs=-1) # *args
@click.option("-v", "--verbose", is_flag=True, help="increase output verbosity")
@click.option("-m",  "--mode", required=True, help="the calculation mode: add | sub | mul | div")
def calculate(numbers: tuple[int], mode: str, verbose: bool=False) -> None:
    """An example cli created with Click to + | - | * | / 2 or more numbers."""
    if verbose:
        click.echo(f"this is from args: {mode} {numbers}.")
    
    match mode:
        case "add":
            add(numbers)
        case "sub":
            sub(numbers)
        case "mul":
            mul(numbers)
        case "div":
            div(numbers)
        case _:
            click.echo(f"please run the program againg with a calculation mode.")

def add(numbers: tuple[int]) -> None:
    sum = 0
    for num in numbers:
        sum += num
    click.echo(sum)

def sub(numbers: tuple[int]) -> None:
    """Subtract elements in a list of numbers.
    Starting from the 1st elementt - 2nd element, then - 3rd element ... nth element
    """
    result = numbers[0] # set result to the 1st element
    for num in numbers:
        result -= num
    result += numbers[0]
    click.echo(result)

def mul(numbers: tuple[int]) -> None:
    result = 1
    for num in numbers:
        result *= num
    click.echo(result)

def div(numbers: tuple[int]) -> None:
    try:
        result = numbers[0]
        for num in numbers:
            result /= num
        result *= numbers[0]
        click.echo(result)
    except ZeroDivisionError:
        click.echo(f"error: cannot /0")

if __name__=="__main__":
    # with_argv()
    # with_argparse()
    calculate()