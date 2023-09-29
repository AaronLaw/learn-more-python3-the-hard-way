# Here we use `sys.argv` to get argument from stdin
import sys
from typing import List

args: List = sys.argv
print(args)
print(f'The file itself is: {args[0]}')


# Here we use `argparse` to get argument from stdin
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Show Output")

args = parser.parse_args()
if args.output:
    print(f"this is from args 'output': {args.output}")