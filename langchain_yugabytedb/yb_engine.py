from __future__ import annotations

import asyncio
from threading import Thread
from typing import Optional


from sqlalchemy.ext.asyncio import AsyncEngine
from langchain_postgres.v2.engine import PGEngine

class YBEngine(PGEngine):
    """YugabyteDB Engine for LangChain."""
    
    def __init__(
        self,
        key: object,
        pool: AsyncEngine,
        loop: Optional[asyncio.AbstractEventLoop],
        thread: Optional[Thread],
    ) -> None:
        super().__init__(key, pool, loop, thread)

    @property
    def name(self) -> str:
        """Return the name of the engine."""
        return "YugabyteDB"
    
    @property
    def dialect(self) -> str:
        """Return the SQL dialect used by YugabyteDB."""
        return "yugabytedb"
    