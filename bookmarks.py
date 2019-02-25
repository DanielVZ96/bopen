import os
import json
BOOKMARKS_PATH = os.environ.get('BOOKMARKS', None)

def get_bookmarks(bookmarks_folder='bookmark_bar'):
    bookmarks_file_path = BOOKMARKS_PATH
    if bookmarks_file_path is None:
        return None
    with open(bookmarks_file_path) as bookmarks_file:
        bookmarks_data = json.load(bookmarks_file)
        bookmarks = [
            (bookmark['name'], bookmark['url'])
            for bookmark in bookmarks_data['roots'][bookmarks_folder]['children']
            if not bookmark['name'] == ''
        ]
    return bookmarks


