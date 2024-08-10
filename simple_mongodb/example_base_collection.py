from typing import Any, Literal

from .exceptions import Exceptions


class BaseCollection(Exceptions):
    def __init__(self) -> None:
        self.collection: str = 'base-collection'

    async def find(
        self, where: dict[str, Any] = {}, skip: int = 0, limit: int = 25
    ) -> list[dict[str, Any]]:
        raise NotImplementedError

    async def find_one(self, where: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

    async def insert_one(self, document: dict[str, Any]) -> None:
        raise NotImplementedError

    async def insert_many(self, documents: list[dict[str, Any]]) -> None:
        raise NotImplementedError

    async def update_one(
        self, where: dict[str, Any], update: dict[str, Any], upsert: bool = False
    ) -> None:
        raise NotImplementedError

    async def update_many(
        self, where: dict[str, Any], update: dict[str, Any], upsert: bool = False
    ) -> None:
        raise NotImplementedError

    async def delete_one(self, where: dict[str, Any]) -> None:
        raise NotImplementedError

    async def delete_many(self, where: dict[str, Any]) -> None:
        raise NotImplementedError

    async def aggregate(
        self, pipeline: list[dict[str, Any]], limit: int = 25
    ) -> list[dict[str, None]]:
        raise NotImplementedError

    async def create_index(
        self,
        overide: bool = True,
        retry_on_fail: bool = True,
        retry_attempts: int | None = None,
        retry_interval: int = 5000,
        background: bool = True,
    ) -> None:
        raise NotImplementedError

    async def create_simple_index(
        self,
        index: str,
        name: str,
        sort: Literal[1, -1] = 1,
        unique: bool = False,
        sparse: bool = True,
        partialFilterExpression: None | dict[str, Any] = None,
    ) -> None:
        raise NotImplementedError

    async def create_compound_index(
        self,
        indexes: list[tuple[str, Literal[1, -1]]],
        name: str,
        unique: bool = False,
        sparse: bool = True,
        partialFilterExpression: None | dict[str, Any] = None,
    ) -> None:
        raise NotImplementedError

    async def create_ttl_index(
        self,
        index: str,
        name: str,
        expireAfterSeconds: int,
        sort: Literal[1, -1] = 1,
        sparse: bool = True,
        partialFilterExpression: None | dict[str, Any] = None,
    ) -> None:
        raise NotImplementedError

    async def drop_index(self, index_or_name: str) -> None:
        raise NotImplementedError

    async def drop_collection(self) -> None:
        raise NotImplementedError

    async def drop_collection(self) -> None:
        raise NotImplementedError
