from pathlib import Path
import sys
from typing import List, Union, Any, Optional

import click

class Cat:
    def __init__(self, filenames, numbers):
        self.filenames: tuple[click.Path] = filenames
        self.numbers: bool = numbers
        self.line_number: int = 1

    def execute(self) -> None:
        for filename in self.filenames:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if self.numbers:
                    for line in lines:
                        click.echo(f"{self.line_number}\t {line}", nl=False)
                        self.line_number += 1
                else:
                    click.echo(''.join(lines))


class Find:
    """An implementation of `find`.
    """
    def __init__(self, path: str, filename: str, type: str) -> None:
        self.check_required(filename, type)
        
        self.path: Path = Path(path)
        self.filename: str = filename
        self.type: str = type

    def execute(self) -> None:
        # here we dispatch the task
        if self.filename and not self.type:
            self.name_find()
        elif self.type:
            self.type_find()

    def check_required(self, filename: str, type: str) -> None:
        """Check if parameters meet program running requirement.
        if not, exit the program.
        """
        if not filename and not type:
            print(f"You need either -name or -type")
            sys.exit(1)
    
    def name_find(self) -> None:
        for item in self.path.rglob(self.filename):
            print(item)
            
    def type_find(self) -> None:
        self.check_type()

        for item in self.path.rglob(self.filename):
            if self.type == 'd' and not item.is_dir():
                continue
            elif self.type == 'f' and not item.is_file():
                continue
            print(item)
            
    def check_type(self) -> None:
        if self.type not in ['d', 'f']:
            print(f"Unknow type: {self.type}")
            sys.exit(1)


class ReturnFind(Find):
    """An implementation of `find` with return.
    """
    def execute(self) -> List[Path]:
        # here we dispatch the task
        if self.filename and not self.type:
            paths = self.name_find()
        elif self.type:
            paths = self.type_find()
        return paths

    def name_find(self) -> List[Path]:
        return [item for item in self.path.rglob(self.filename)]

    def type_find(self) -> List[Path]:
        self.check_type()
        paths = []

        for item in self.path.rglob(self.filename):
            if self.type == 'd' and not item.is_dir():
                continue
            elif self.type == 'f' and not item.is_file():
                continue
            paths.append(item)
        return paths


class BookmarkToMarkdown:
    def __init__(self, path, fetch_line_number, extension, out_file):
        self.path = Path(path)
        self.line_number = fetch_line_number
        self.extension = extension
        self.out_file = out_file

        self.find = ReturnFind(self.path, self.extension, 'f')
        self.entries = []

    def execute(self) -> None:
        # get all the files ending '.url' in a directory

        # process them one by one
            # get the filename
            # open the file
            # read the 2nd line, which is the URL
            # open a new file
            # write in [{filename}]({URL}) format, as markdown syntax
            # write chuck of data into file
        bookmark_list: List[Path] = self.find.execute()
        for item in bookmark_list:
            # print(type(item))
            stem: str = self.get_filename(item)
            contents: List[str] = self.get_contents(item)
            url: str = self.get_url(contents)
            entry: str = self.format_as_markdown(stem, url, line_break=True)
            self.entries.append(entry)
        self.write_file()


    def get_filename(self, path) -> str:
        """Return the filename part from a Path.
        """
        return path.stem

    def get_contents(self, path) -> list[str]:
        """Given a path and return its contents.
        """
        with open(path, 'r') as file:
            return file.readlines()

    def get_url(self, lines) -> str:
        """Given a content and return a line.
        """
        url = lines[self.line_number-1].rstrip()[4:]
        return url

    def format_as_markdown(self, link_text, url, line_break: bool = False) -> str:
        if line_break:
            return f"- [{link_text}]({url})\n"
        return f"- [{link_text}]({url})"

    def write_file(self) -> None:
        with open(self.out_file, 'w') as f:
            f.writelines(self.entries)
