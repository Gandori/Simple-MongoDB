# Simple-MongoDB

## Description

This asynchronous Python package streamlines the management and manipulation of MongoDB collections. It offers built-in support for creating, reading, updating, and deleting documents, as well as comprehensive index management. Featuring a clean and efficient interface, it integrates seamlessly with asyncio to support non-blocking operations and maximize performance in asynchronous applications.

## Example idea to use it

#### Easy to create a collection

```python
from simple_mongodb import BaseCollection


class ExampleCollection(BaseCollection):
    def __init__(self) -> None:
        self.collection = 'example-collection'  # The name of the collection


example_collection: ExampleCollection = ExampleCollection()
```
