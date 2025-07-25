# TODO: Remove below import when minimum supported Python version is 3.10
from __future__ import annotations

from typing import Optional, Sequence

from langchain_core.embeddings import Embeddings

from langchain_postgres.v2.vectorstores import PGVectorStore
from langchain_postgres.v2.engine import PGEngine
from langchain_yugabytedb.async_vectorstore import AsyncYugabyteDBVectorStore
from langchain_yugabytedb.yb_engine import YBEngine


class YugabyteDBVectorStore(PGVectorStore):
    """YugabyteDB Vector Store class."""
    
    def __init__(
        self,
        key: object,
        engine: YBEngine,
        vs: AsyncYugabyteDBVectorStore,
    ) -> None:
        
        """Initialize YugabyteDB Vector Store."""    
        super().__init__(

            key=key,
            engine=engine,
            vs=vs,
        )