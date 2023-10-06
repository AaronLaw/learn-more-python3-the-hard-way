from typing import Union, Any, Optional
from Command import BookmarkToMarkdown

import click

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='bookmarks.md', help='The output filename [default: bookmarks.md]')
@click.option('-w', '--over-write', is_flag=True, show_default=True, default=False,
              help='Over-write an existing output file [default: false]')
def bookmark_to_markdown(path: click.Path, output: str, over_write: bool):
    """Convert bookmark files to a single markdown file.
    """
    # path = '/home/aaron/Music/reload/'
    fetch_line_number = 2
    file_suffix = "*.URL"
    # out_filename = "bookmarks.md"
    BookmarkToMarkdown(path, fetch_line_number, file_suffix, output, over_write).execute()

if __name__=="__main__":
    bookmark_to_markdown()