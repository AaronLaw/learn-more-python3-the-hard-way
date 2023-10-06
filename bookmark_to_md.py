from typing import Union, Any, Optional
from Command import BookmarkToMarkdown

import click

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='bookmarks.md', help='The output filename')
def bookmark_to_markdown(path: click.Path, output: str):
    """Convert bookmark files to a single markdown file.
    """
    # path = '/home/aaron/Music/reload/'
    fetch_line_number = 2
    file_suffix = "*.URL"
    # out_filename = "bookmarks.md"
    BookmarkToMarkdown(path, fetch_line_number, file_suffix, output).execute()

if __name__=="__main__":
    bookmark_to_markdown()