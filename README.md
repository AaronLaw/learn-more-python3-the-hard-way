# Readme

This is a long-running project that I will go to (re)implement some UNIX commands with a book "Learn more Python the hard way" to learn to program better.

3 things to be bear in mind:
1. process
2. creativity
3. quality

## Quick hacks

Organization: program comments should be put in README rather than be put in the python script. (a.k.a. don't make dead code nor unintentional comments in the script.)

## Dealing with command line arguments

- [x] on research how to get command line arguments from a user
    - [x] with `sys.argv`
    - [x] with `argparse`
    - [x] with `click`
        - [x] try more options with `click` 
    - [x] extend the `add(a, b)` to `add(a, b, ..., n)` (a.k.a. passing `*args` to function)

Some basics functions which all CLIs have are:
- An argument. (positional argument)
- An option, which is an optional parameter
- A flag, this is a special option which enables or disables a certain function. One of the most common flags is –help.

reference:
- how to work with sys.argv?
    - Google: sys.argv -> [How to use sys.argv in Python - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/) for study on sys.argv, argparse, click
- how to work with argparse?
    - Google: argparse -> https://docs.python.org/3/library/argparse.html
- how to add program description with click? (e.g. "this program adds 2 given numbers...")
    - Google: python click program description -> [The Definitive Guide to Python Click](https://www.assemblyai.com/blog/the-definitive-guide-to-python-click/#:~:text=Click%2C%20or%20“Command%20Line%20Interface,loading%20of%20subcommands%20at%20runtime.)
- how to work with `*args` with Click?
    - Google: click *args -> [Variadic Arguments](https://click.palletsprojects.com/en/8.1.x/arguments/)
- given a list of numbers. how to subtract from the 1st element, then 2nd element, then the nth element?
    - poe: python doing subtraction in a list elements. from first element - second element - thrid element

for doing subtraction elements in a list: (answered by poe)
```python
numbers = [10, 5, 3, 1]
result = numbers[0]  # Set the initial result to the first element

for i in range(1, len(numbers)):
    result -= numbers[i]  # Subtract each subsequent element

print(result)  # Output: 1
```

or 
```python
numbers = [10, 5, 3, 1]
result = numbers[0] - sum(numbers[1:])

print(result)  # Output: 1
```

### The concepts of click

click uses decorator to wrap function to a Command [^click]
=> I write function 1st, then make it into Command.

[^click]: Python Command Line Tools by Noah Gift 

### Reflection

Finding out what blocks me to work on:
- At first, I am **lazy to figure out** / to study how argparse works.
- When I try to make a MVP with Click, the script doesn't work at first. -> I am afraid of reading onlarge pages of documentation of any 3rd party projects.
    - The solution is quite simple: The concept behind Click is turing python function into a Command with the `@click` decorator.
    - the problem of mine is: I have an option `--verbose` but I haven't notice I have to put it in function signature at 1st because I have no idea the concept behind Click is turning python function into a Command (it is because **I haven't read through** Click's documentation):
        - `def add(first, second)` => `def add(first, second, verbose=False)` 


## cat

Click turns Python function into Command.
What if I write the `cat` as a class?

- [x] make it as class

### Reflection

Finding out what blocks me to work on:

## find

`find` has lots of parameters, and here I go to implement the following features:
- [x] given `.` or some path (e.g. /usr/local/)
- [x] a filter: e.g. `-name` or `-type d` (file of directory type)
- [x] the operation on each matching file: `-print`

A simple test case is to find the files with `.txt` in the current directory and print them out: `find -name "*.txt" -print`

### `glob`

Give it a path, `glob` lists all files & directory in the path (a.k.a. 1 level) while `rglob` does it recursively.

reference:
- How to Get a List of All Files in a Directory With Python
    - [How to Get a List of All Files in a Directory With Python – Real Python](https://realpython.com/get-all-files-in-directory-python/)

### Reflection

Finding out what blocks me to work on:
from confusion => understanding

1. At 1st, I confuse on the implementation and go to see the "model answer" [^1] from the author (a.k.a. the code on Github)
    1. I try to figure out the logic & data flow of the code, and then I still feeling of confusion
    2. Then I write a backbone / the basic structure of the `find` command in OOP style: hope to help me less confuse and it doesn't
2. I re-read the question again and again from the webpage [^2]. It actually help me less confusion
    1. I use my own word to re-write the question / the requirement as a main sentence, and followed a list of [x] as sub-tasks.
    2. This help me understand what should I do, and what I am going to implement (a main theme and sub-tasks)

[^1]: https://github.com/zedshaw/learn-more-python-the-hard-way-solutions
[^2]: https://learncodethehardway.org/more-python-book/ex6.html

### After work hints

- poe: can you implement linux's find in python? with the use of Pathlib and Click. make it class.


## BookmarkToMarkdown

Problem statement:
I use Linux as my daily driver, and sometimes I web surfing on a Windows machine and I have drop URLs as browser bookmark files (*.URL). I want to move these bookmark files in a managable formation. Make them all as one markdown file is good enough.


reference:
- python read file
- python read the second line of a file -> https://pynative.com/python-read-specific-lines-from-a-file/
- python remove '\n' from readlines -> https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
- python remove first few characters of readlines -> https://stackoverflow.com/questions/18924761/remove-first-char-from-each-line-in-a-text-file

To handle line element in a file (code in function `BookmarkToMarkdown.get_url`):

To assign the 2nd line to url
```python
url = file.readlines()[1]
```
To assign the 2nd~4th line to url
```python
url = file.readlines()[1:3]
```
To remove the ending `\n` of a line
```python
url = file.readlines()[1].rstrip()
```
 To remove the first 4 characters, which are "URL="
```python
url = file.readlines()[1].rstrip()[4:]
```