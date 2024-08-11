from functools import wraps
from typing import Any, Callable

from bson import ObjectId
from motor.core import AgnosticCursor
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError, ServerSelectionTimeoutError
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult

from .exceptions import Exceptions
from .mongodb_client_settings import MongoDBClientSettings


def exception_decorator(
    exception: type[Exception],
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return await func(*args, **kwargs)
            except DuplicateKeyError as e:
                raise Exceptions.DuplicateKeyError(e)
            except ServerSelectionTimeoutError as e:
                raise Exceptions.ServerTimeoutError(e)
            except Exception as e:
                raise exception(e)

        return wrapper

    return decorator


class MongoDBClient:
    def __init__(self, settings: MongoDBClientSettings) -> None:
        self.client: AsyncIOMotorClient[Any] = AsyncIOMotorClient(
            settings.url,
            serverSelectionTimeoutMS=settings.response_timeout,
            connectTimeoutMS=settings.connection_timeout,
        )

    @exception_decorator(exception=Exceptions.FindError)
    async def find(
        self,
        db: str,
        collection: str,
        where: dict[str, Any] = {},
        skip: int = 0,
        limit: int = 25,
    ) -> list[dict[str, Any]]:
        cursor: AgnosticCursor[Any] = self.client[db][collection].find(where)
        return await cursor.skip(skip=skip).to_list(length=limit)  # type: ignore

    @exception_decorator(exception=Exceptions.FindError)
    async def find_one(
        self, db: str, collection: str, where: dict[str, Any]
    ) -> dict[str, Any]:
        result: dict[str, Any] | None = await self.client[db][collection].find_one(
            where
        )
        if not result:
            raise Exceptions.NotFoundError('The document was not found')
        return result

    @exception_decorator(exception=Exceptions.InsertError)
    async def insert_one(
        self, db: str, collection: str, document: dict[str, Any]
    ) -> ObjectId:
        result: InsertOneResult = await self.client[db][collection].insert_one(document)
        return result.inserted_id

    @exception_decorator(exception=Exceptions.UpdateError)
    async def update_one(
        self,
        db: str,
        collection: str,
        where: dict[str, Any],
        update: dict[str, Any],
        upsert: bool = False,
    ) -> ObjectId | None:
        result: UpdateResult = await self.client[db][collection].update_one(
            filter=where, update=update, upsert=upsert
        )
        return result.upserted_id

    @exception_decorator(exception=Exceptions.DeleteError)
    async def delete_one(
        self, db: str, collection: str, where: dict[str, Any]
    ) -> DeleteResult:
        return await self.client[db][collection].delete_one(where)

    @exception_decorator(exception=Exceptions.DropCollectionError)
    async def drop_collection(self, db: str, collection: str) -> None:
        await self.client[db][collection].drop()
