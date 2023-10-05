from pathlib import Path
from Command import Find

class BookmarkToMarkdown:
    def __init__(self, path, fetch_line_number, extension):
        self.path = Path(path)
        self.line_number = fetch_line_number
        self.extension = extension

        self.find = Find(self.path, self.extension, 'f')

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
            print(f"- [{stem}]({url})")
            # self.write_markdown()

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

    def write_markdown(self) -> None:
        pass


if __name__=="__main__":
    path = '/home/aaron/Music/reload/'
    fetch_line_number = 2
    file_end = "*.URL"

    BookmarkToMarkdown(path, fetch_line_number, file_end).execute()
