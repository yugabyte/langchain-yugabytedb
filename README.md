# langchain-yugabytedb

The `langchain-yugabytedb` package implementations of core LangChain abstractions using `YugabyteDB` Distributed SQL Database.

The package is released under the MIT license.

Feel free to use the abstraction as provided or else modify them / extend them as appropriate for your own application.

## Requirements

The package supports the [asyncpg](https://github.com/MagicStack/asyncpg) and [psycopg3](https://www.psycopg.org/psycopg3/) drivers.

## Installation

```bash
pip install -U langchain-yugabytedb
```

### Documentation

* [Quickstart](https://docs.yugabyte.com/preview/explore/ysql-language-features/pg-extensions/extension-pgvector/#hnsw)

### Example

```python
from langchain_core.documents import Document
from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_yugabytedb import YBEngine, YugabyteDBVectorStore

# Replace the connection string with your own YugabyteDB connection string
CONNECTION_STRING = "postgresql+psycopg://yugabyte:@localhost:5433/yugabyte"
engine = YBEngine.from_connection_string(url=CONNECTION_STRING)

# Replace the vector size with your own vector size
VECTOR_SIZE = 768
embedding = DeterministicFakeEmbedding(size=VECTOR_SIZE)

TABLE_NAME = "my_doc_collection"

engine.init_vectorstore_table(
    table_name=TABLE_NAME,
    vector_size=VECTOR_SIZE,
)

store = YugabyteDBVectorStore.create_sync(
    engine=engine,
    table_name=TABLE_NAME,
    embedding_service=embedding,
)

docs = [
    Document(page_content="Apples and oranges"),
    Document(page_content="Cars and airplanes"),
    Document(page_content="Train")
]

store.add_documents(docs)

query = "I'd like a fruit."
docs = store.similarity_search(query)
print(docs)
```

> [!TIP]
> All synchronous functions have corresponding asynchronous functions

## ChatMessageHistory

The chat message history abstraction helps to persist chat message history
in a YugabyteDB table.

YugabyteDBChatMessageHistory is parameterized using a `table_name` and a `session_id`.

The `table_name` is the name of the table in the database where
the chat messages will be stored.

The `session_id` is a unique identifier for the chat session. It can be assigned
by the caller using `uuid.uuid4()`.

```python
import uuid

from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_yugabytedb import YugabyteDBChatMessageHistory
import psycopg

# Establish a synchronous connection to the database
# (or use psycopg.AsyncConnection for async)
conn_info = ... # Fill in with your connection info
sync_connection = psycopg.connect(conn_info)

# Create the table schema (only needs to be done once)
table_name = "chat_history"
YugabyteDBChatMessageHistory.create_tables(sync_connection, table_name)

session_id = str(uuid.uuid4())

# Initialize the chat history manager
chat_history = YugabyteDBChatMessageHistory(
    table_name,
    session_id,
    sync_connection=sync_connection
)

# Add messages to the chat history
chat_history.add_messages([
    SystemMessage(content="Meow"),
    AIMessage(content="woof"),
    HumanMessage(content="bark"),
])

print(chat_history.messages)
```
