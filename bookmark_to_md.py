from typing import Union, Any, Optional
from Command import BookmarkToMarkdown


if __name__=="__main__":
    path = '/home/aaron/Music/reload/'
    fetch_line_number = 2
    file_end = "*.URL"
    out_filename = "bookmarks.md"

    BookmarkToMarkdown(path, fetch_line_number, file_end, out_filename).execute()
