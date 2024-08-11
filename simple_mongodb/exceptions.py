class Exceptions:
    class FindError(Exception):
        pass

    class FindOneError(Exception):
        pass

    class NotFoundError(Exception):
        pass

    class InsertError(Exception):
        pass

    class DuplicateKeyError(Exception):
        pass

    class AggregateError(Exception):
        pass

    class UpdateError(Exception):
        pass

    class DeleteError(Exception):
        pass

    class CreateIndexError(Exception):
        pass

    class DropIndexError(Exception):
        pass

    class ServerTimeoutError(Exception):
        pass

    class DropCollectionError(Exception):
        pass
