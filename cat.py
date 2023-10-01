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

def cat():
    with open('text.txt', 'rt') as f:
        for line in f:
            print(line)

if __name__=="__main__":
    cat()