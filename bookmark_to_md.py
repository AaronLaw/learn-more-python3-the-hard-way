
from Command import Find

def bookmark_to_md(path):
    # get all the files ending '.url' in a directory

    # process them one by one
        # get the filename
        # open the file
        # read the 2nd line, which is the URL
        # write in [{filename}]({URL}) to markdown syntax
        # write into file
        find = Find(path, '*.URL', 'f')
        bookmark_list = find.execute()
        for item in bookmark_list:
            print((item))

if __name__=="__main__":
    path = '/home/aaron/Music/reload/'
    bookmark_to_md(path)