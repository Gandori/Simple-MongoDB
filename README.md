# Simple-MongoDB

> Warning: This Python package is currently still in development phase

## Description

This asynchronous Python package streamlines the management and manipulation of MongoDB collections. It offers built-in support for creating, reading, updating, and deleting documents, as well as comprehensive index management. Featuring a clean and efficient interface, it integrates seamlessly with asyncio to support non-blocking operations and maximize performance in asynchronous applications.

## MongoDB Connection Configuration

This Python package offers flexible options for configuring the MongoDB connection. In addition to using environment variables, you can also set connection parameters directly within your code. This allows for easy customization of settings according to your needs.

Environment variables provide a secure and adaptable method for managing connection details such as the URI and database name. Alternatively, you can define configuration settings programmatically in your code. Both methods support flexible integration and customization of the package in your environment.

Note: If environment variables are set, they will be used; however, if connection settings are also defined in the code, those will take precedence. This ensures that your preferred method of configuration is applied without causing any conflicts.

### Environment Variables

| Variable Name | Type | Default Value | Description |
| - | - | - | - |
| MONGODB_HOST | string | localhost | The hostname or IP address of the MongoDB server. |
| MONGODB_PORT | int | 27017 | The port number on which the MongoDB server is listening. |
| MONGODB_USERNAME | string | user | The username used for authentication with the MongoDB server. |
| MONGODB_PASSWORD | string | user | The password used for authentication with the MongoDB server. |
| MONGODB_DB | string | example | The name of the database to connect to within MongoDB. |
| MONGODB_RESPONSE_TIMEOUT | int | 5000 | The maximum time (in milliseconds) to wait for a response from MongoDB. |
| MONGODB_CONNECTION_TIMEOUT | int | 5000 | The maximum time (in milliseconds) to establish a connection to MongoDB. |

### With Code

```python
```

### Examples

#### Create a collection

```python
from simple_mongodb import BaseCollection


class ExampleCollection(BaseCollection):
    collection = 'example-collection'  # The name of the collection
```
