from pathlib import Path
import sys
import datetime
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
    """Convert bookmark file (drops on Windows) into one markdown file.

    reserve information:
        - filename
        - URL
        - st_mtime
    """
    def __init__(self, path: str, fetch_line_number: int, extension: str,
                 out_file: str, over_write: bool, mtime: bool):
        self.path = Path(path)
        self.line_number = fetch_line_number
        self.extension = extension
        self.out_file = Path(out_file)
        self.over_write  = over_write
        self.mtime = mtime

        self.find = ReturnFind(self.path, self.extension, 'f')
        self.entries = []

    def execute(self) -> None:
        self.check_output_exist()
        # get all the files ending '.url' in a directory
        bookmark_list: List[Path] = self.find.execute()

        # process them one by one
            # get the filename
            # open the file
            # read the 2nd line, which is the URL
            # open a new file
            # write in [{filename}]({URL}) format, as markdown syntax
            # write chuck of data into file
        for item in bookmark_list:
            # print(type(item))
            stem: str = self.get_filename(item)
            contents: List[str] = self.get_contents(item)
            line: str = self.get_line(contents)
            url: str = self.get_line(line)
            if self.mtime:
                mtime: datetime.datetime = self.get_modify_datetime(item)
                entry: str = self.format_as_markdown_with_mtime(stem, url, mtime,line_break=True)
            else:
                entry: str = self.format_as_markdown(stem, url, line_break=True)
            self.entries.append(entry)
        self.write_file()


    def get_filename(self, path: str) -> str:
        """Return the filename part from a Path.
        """
        return path.stem

    def get_contents(self, path: str) -> list[str]:
        """Given a path and return its contents.
        """
        with open(path, 'r') as file:
            return file.readlines()

    def get_line(self, lines: List[str]) -> str:
        """Given a list of contents and return a line.
        """
        line = lines[self.line_number-1]
        return line
    
    def get_url(self, line: str) -> str:
        """Pick the part which is URL from a string.
        """
        return line.rstrip()[4:]

    def format_as_markdown(self, link_text: str, url: str, line_break: bool=False) -> str:
        if line_break:
            return f"- [{link_text}]({url})\n"
        return f"- [{link_text}]({url})"
    
    def format_as_markdown_with_mtime(self, link_text: str, url: str, mtime: str, line_break: bool=False) -> str:
        if line_break:
            return f"- {mtime} - [{link_text}]({url})\n"
        return f"- {mtime} - [{link_text}]({url})"

    def write_file(self) -> None:
        """Write entries of link in markdown format ot a file.
        """
        with open(self.out_file, 'w') as f:
            f.writelines(self.entries)
        print(f"{self.extension} has been written into {self.out_file} successfully.")

    def check_output_exist(self) -> None:
        """Handle the case where output file exist.
        
        If output file exists and over-write is not allowed
        then exit.
        """
        if Path.exists(self.out_file) and not self.over_write:
            print(f"{self.out_file} exists: No over-write.")
            sys.exit(1)

    def get_modify_datetime(self, path: str) -> datetime.datetime:
        """Get the st_mtime of a Path.
        """
        epoch_time = Path(path).stat().st_mtime
        date_time = datetime.datetime.fromtimestamp(epoch_time)

        format='%Y-%m-%d %H:%M:%S'
        return date_time.strftime(format)