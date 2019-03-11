# Bopen
Open bookmarks from the shell

## TODO
- [ ] Implement logging.
- [ ] Linux support:
  - [ ] Add/update/test linux bookmarks location in `bookmarks.py`
  - [ ] Detect defaults in linux in `os_helpers.py`
- [ ] Suport Firefox: (Hint: `SELECT moz_places.url, moz_bookmarks.title FROM moz_places INNER JOIN moz_bookmarks ON moz_places.id=moz_bookmarks.fk WHERE moz_bookmarks.title NOTNULL` in .mozilla)
- [ ] Tests
- [ ] Tox and packaging
