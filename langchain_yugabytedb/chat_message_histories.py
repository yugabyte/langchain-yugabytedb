"""Client for persisting chat message history in a YugabyteDB database.

This client provides support for both sync and async via psycopg 3.
"""

from __future__ import annotations

import logging
from typing import List, Optional, Sequence

import psycopg
from langchain_postgres.chat_message_histories import PostgresChatMessageHistory

logger = logging.getLogger(__name__)

class YugabyteDBChatMessageHistory(PostgresChatMessageHistory):
    """YugabyteDB Vector Store for chat message history.

    This class extends PostgresChatMessageHistory to provide YugabyteDB specific
    functionality. It uses the same schema and methods as PostgresChatMessageHistory.
    """

    def __init__(
        self,
        table_name: str,
        session_id: str,
        /,
        sync_connection: Optional[psycopg.Connection] = None,
        async_connection: Optional[psycopg.AsyncConnection] = None,
    ) -> None:
        super().__init__(table_name, session_id, sync_connection=sync_connection, async_connection=async_connection)
