from .exceptions import Exceptions


class BaseCollection(Exceptions):
    def __init__(self) -> None:
        self.collection: str = 'base-collection'
