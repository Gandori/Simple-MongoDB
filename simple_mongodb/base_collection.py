from typing import Any

from bson import ObjectId

from .exceptions import Exceptions
from .mongodb_client import MongoDBClient
from .mongodb_client_settings import MongoDBClientSettings


class BaseCollection(Exceptions):
    __initialized: bool = False
    __client_settings: MongoDBClientSettings

    client: MongoDBClient
    db: str
    collection: str

    def __init__(self) -> None:
        if not BaseCollection.__initialized:
            BaseCollection.__initialized = True
            BaseCollection.__client_settings = MongoDBClientSettings()
            BaseCollection.client = MongoDBClient(settings=self.__client_settings)

        if not hasattr(self, 'db'):
            self.db = self.__client_settings.db

    def __init_subclass__(cls) -> None:
        if '__init__' in cls.__dict__:
            raise TypeError(
                f"The subclass '{cls.__name__}' of BaseCollection is not allowed to override __init__"
            )

        if hasattr(cls, 'client'):
            raise NotImplementedError(
                f"The subclass '{cls.__name__}' of BaseCollection currently does not support the value 'client'"
            )

        if hasattr(cls, 'db'):
            if not isinstance(cls.db, str):  # type: ignore
                raise TypeError(
                    f"The 'db' value in subclass '{cls.__name__}' of BaseCollection must be a string"
                )

        if not hasattr(cls, 'collection'):
            raise ValueError(
                f"The subclass '{cls.__name__}' of BaseCollection must define 'collection'"
            )

        if not isinstance(cls.collection, str):  # type: ignore
            raise TypeError(
                f"The 'collection' value in subclass '{cls.__name__}' of BaseCollection must be a string"
            )

    async def find_one(self, where: dict[str, Any]) -> dict[str, Any]:
        '''
        Find one document in the collection.

        Args:
            where (dict) : A dictionary specifying the criteria for finding the document.

        Raises:
            NotFoundError: If the document not find.
            FindOneError: If an error occurs while finding the document.
        '''

        return await self.client.find_one(
            db=self.db, collection=self.collection, where=where
        )

    async def find(
        self, where: dict[str, Any] = {}, skip: int = 0, limit: int = 25
    ) -> list[dict[str, Any]]:
        '''
        Find documents in the collection.

        Args:
            where (dict): A dictionary specifying the criteria for finding the documents.
            skip (int, optional): The number of documents to skip before starting to return results. Defaults to 0.
            limit (int, optional): The maximum number of documents to return. Defaults to 25.

        Raises:
            FindOneError: If an error occurs while finding the documents.
        '''

        return await self.client.find(
            db=self.db, collection=self.collection, where=where, skip=skip, limit=limit
        )

    async def insert_one(self, document: dict[str, Any]) -> ObjectId:
        '''
        Insert one document into the collection.

        Args:
            document (dict): The document to be inserted into the collection.

        Returns:
            ObjectId: The ObjectId of the inserted document.

        Raises:
            InsertError: If an error occurs while inserting the document.
            DuplicateKeyError: If the document cannot be inserted due to a duplicate key constraint violation.
        '''

        return await self.client.insert_one(
            db=self.db, collection=self.collection, document=document
        )

    async def update_one(
        self, where: dict[str, Any], update: dict[str, Any], upsert: bool = False
    ) -> ObjectId | None:
        '''
        Update one document in the collection.

        Args:
            where (dict): A dictionary specifying the criteria for finding the document to update.
            update (dict): A dictionary specifying the fields and values to update in the document.
            upsert (bool, optional): Whether to insert the document if it does not exist. Defaults to False.

        Raises:
            UpdateError: If an error occurs while updating the document.
            DuplicateKeyError: If the document cannot be inserted due to a duplicate key constraint violation.
        '''

        return await self.client.update_one(
            db=self.db,
            collection=self.collection,
            where=where,
            update=update,
            upsert=upsert,
        )

    async def drop_collection(self) -> None:
        '''
        Drop the collection from the database

        Raises:
            DropCollectionError: if an error occurs while dropping the collection
        '''
        await self.client.drop_collection(db=self.db, collection=self.collection)
