# services.py

from djbarky.adapters.repository import AbstractRepository
from djbarky.domain import models as domain_models

class BookmarkService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def add_bookmark(self, title: str, url: str, notes: str):
        bookmark = domain_models.Bookmark(title=title, url=url, notes=notes)
        self.repository.add(bookmark)
        return bookmark

    def list_bookmarks(self):
        return self.repository.list()

    def get_bookmark(self, bookmark_id: int):
        return self.repository.get(bookmark_id)
