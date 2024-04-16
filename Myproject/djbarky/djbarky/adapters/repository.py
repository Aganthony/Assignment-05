# repositories.py (interface for the repository)

from abc import ABC, abstractmethod
from typing import List
from djbarky.domain import models as domain_models

class AbstractRepository(ABC):

    @abstractmethod
    def add(self, bookmark: domain_models.Bookmark):
        raise NotImplementedError

    @abstractmethod
    def get(self, bookmark_id: int) -> domain_models.Bookmark:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[domain_models.Bookmark]:
        raise NotImplementedError
