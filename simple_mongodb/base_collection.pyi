from typing import Any, Dict, List, Optional

from bson import ObjectId

from .exceptions import Exceptions
from .mongodb_client import MongoDBClient
from .mongodb_client_settings import MongoDBClientSettings

class BaseCollection(Exceptions):
    __initialized: bool
    __client_settings: MongoDBClientSettings

    client: MongoDBClient
    db: str
    collection: str

    def __init__(self) -> None: ...
    @classmethod
    def __init_subclass__(cls) -> None: ...
    async def find_one(self, where: Dict[str, Any]) -> Dict[str, Any]: ...
    async def find(
        self, where: Optional[Dict[str, Any]] = None, skip: int = 0, limit: int = 25
    ) -> List[Dict[str, Any]]: ...
    async def insert_one(self, document: Dict[str, Any]) -> ObjectId: ...
    async def update_one(
        self, where: Dict[str, Any], update: Dict[str, Any], upsert: bool = False
    ) -> Optional[ObjectId]: ...
    async def drop_collection(self) -> None: ...
