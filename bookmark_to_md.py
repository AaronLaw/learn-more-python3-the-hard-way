from typing import Union, Any, Optional
from Command import BookmarkToMarkdown

import click

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='bookmarks.md', help='The output filename [default: bookmarks.md]')
@click.option('-w', '--over-write', is_flag=True, show_default=True, default=False,
              help='Over-write an existing output file [default: false]')
@click.option('-t', '--timestamp', is_flag=True, default=False, help='add file\'s timestamp')
def bookmark_to_markdown(path: click.Path, output: str, over_write: bool, timestamp: bool):
    """Convert bookmark files to a single markdown file.
    """
    # path = '/home/aaron/Music/reload/'
    fetch_line_number = 2
    file_suffix = "*.URL"
    BookmarkToMarkdown(path, fetch_line_number, file_suffix, output, over_write, timestamp).execute()

if __name__=="__main__":
    bookmark_to_markdown()