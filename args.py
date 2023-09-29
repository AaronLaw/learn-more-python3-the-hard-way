# Here we use `sys.argv` to get argument from stdin
import sys
from typing import List

args: List = sys.argv
print(args)
print(f'The file itself is: {args[0]}')


# Here we use `argparse` to get argument from stdin
import argparse

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