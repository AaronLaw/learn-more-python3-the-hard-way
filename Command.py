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
    """An implementation of `find` with return.
    """
    def __init__(self, path: str, filename: str, type: str) -> None:
        self.check_required(filename, type)
        
        self.path: Path = Path(path)
        self.filename: str = filename
        self.type: str = type

    def execute(self) -> List[Path]:
        # paths = []
        # here we dispatch the task
        if self.filename and not self.type:
            paths = self.name_find()
            # paths = [item for item in self.name_find()]
        elif self.type:
            paths = self.type_find()
            # paths = [item for item in self.type_find()]
        return paths

    def check_required(self, filename: str, type: str) -> None:
        """Check if parameters meet program running requirement.
        if not, exit the program.
        """
        if not filename and not type:
            print(f"You need either -name or -type")
            sys.exit(1)
    
    def name_find(self) -> Path:
        paths = []
        for item in self.path.rglob(self.filename):
            print(item)
            paths.append(item)
        return item
            
    def type_find(self) -> List[Path]:
        self.check_type()
        paths = []

        for item in self.path.rglob(self.filename):
            if self.type == 'd' and not item.is_dir():
                continue
            elif self.type == 'f' and not item.is_file():
                continue
            print(item)
            paths.append(item)
        return paths

    def check_type(self) -> None:
        if self.type not in ['d', 'f']:
            print(f"Unknow type: {self.type}")
            sys.exit(1)