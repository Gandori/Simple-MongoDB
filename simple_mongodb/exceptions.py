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
