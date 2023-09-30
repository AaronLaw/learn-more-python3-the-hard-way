# Readme

This is a long-running project that I will go to (re)implement some UNIX commands with a book "Learn more Python the hard way" to learn to program better.

3 things to be bear in mind:
1. process
2. creativity
3. quality

## Quick hacks

Organization: program comments should be put in README rather than be put in the python script. (a.k.a. don't make dead code nor unintentional comments in the script.)

## Dealing with command line arguments

- [ ] on research how to get command line arguments from a user
    - [x] with `sys.argv`
    - [x] with `argparse`
    - [ ] with `click`

Some basics functions which all CLIs have are:
- An argument. (positional argument)
- An option, which is an optional parameter
- A flag, this is a special option which enables or disables a certain function. One of the most common flags is –help.

reference:
- Google: sys.argv -> [How to use sys.argv in Python - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/) for study on sys.argv, argparse, click
- Google: argparse -> https://docs.python.org/3/library/argparse.html
- Google: python click program description -> [The Definitive Guide to Python Click](https://www.assemblyai.com/blog/the-definitive-guide-to-python-click/#:~:text=Click%2C%20or%20“Command%20Line%20Interface,loading%20of%20subcommands%20at%20runtime.)

### The concepts of click

click uses decorator to wrap function to a Command [^click]
=> I write function 1st, then make it into Command.

[^click]: Python Command Line Tools by Noah Gift 

## cat


