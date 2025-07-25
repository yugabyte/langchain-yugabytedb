"""Get fixtures for the database connection."""

import os
from contextlib import asynccontextmanager, contextmanager

import psycopg
from typing_extensions import AsyncGenerator, Generator

# Env variables match the default settings in the docker-compose file
# located in the root of the repository: [root]/docker-compose.yml
# Non-standard ports are used to avoid conflicts with other local postgres
# instances.
# To spint up the postgres service for testing, run:
# cd [root]/docker-compose.yml
# docker-compose up pgvector
YUGABYTEDB_USER = os.environ.get("YUGABYTEDB_USER", "yugabyte")
YUGABYTEDB_HOST = os.environ.get("YUGABYTEDB_HOST", "localhost")
YUGABYTEDB_PASSWORD = os.environ.get("YUGABYTEDB_PASSWORD", "")
YUGABYTEDB_DB = os.environ.get("YUGABYTEDB_DB", "yugabyte")

YUGABYTEDB_PORT = os.environ.get("YUGABYTEDB_PORT", "5433")

DSN = (
    f"postgresql://{YUGABYTEDB_USER}:{YUGABYTEDB_PASSWORD}@{YUGABYTEDB_HOST}"
    f":{YUGABYTEDB_PORT}/{YUGABYTEDB_DB}"
)

# Connection string used primarily by the vectorstores tests
# it's written to work with SQLAlchemy (takes a driver name)
# It is also running on a postgres instance that has the pgvector extension
VECTORSTORE_CONNECTION_STRING = (
    f"postgresql+psycopg://{YUGABYTEDB_USER}:{YUGABYTEDB_PASSWORD}@{YUGABYTEDB_HOST}"
    f":{YUGABYTEDB_PORT}/{YUGABYTEDB_DB}"
)


@asynccontextmanager
async def asyncpg_client() -> AsyncGenerator[psycopg.AsyncConnection, None]:
    # Establish a connection to your test database
    conn = await psycopg.AsyncConnection.connect(conninfo=DSN)
    try:
        yield conn
    finally:
        # Cleanup: close the connection after the test is done
        await conn.close()


@contextmanager
def syncpg_client() -> Generator[psycopg.Connection, None, None]:
    # Establish a connection to your test database
    conn = psycopg.connect(conninfo=DSN)
    try:
        yield conn
    finally:
        # Cleanup: close the connection after the test is done
        conn.close()
