# TODO: Remove below import when minimum supported Python version is 3.10
from __future__ import annotations

from typing import Optional, Sequence


from langchain_core.embeddings import Embeddings
from sqlalchemy.ext.asyncio import AsyncEngine

from langchain_postgres.v2.async_vectorstore import AsyncPGVectorStore
from langchain_postgres.v2.hybrid_search_config import HybridSearchConfig
from langchain_yugabytedb.indexes import DEFAULT_DISTANCE_STRATEGY, DistanceStrategy, QueryOptions


class AsyncYugabyteDBVectorStore(AsyncPGVectorStore):
    """AsyncYugabyteDB Vector Store class."""
    
    def __init__(
                self,
        key: object,
        engine: AsyncEngine,
        embedding_service: Embeddings,
        table_name: str,
        *,
        schema_name: str = "public",
        content_column: str = "content",
        embedding_column: str = "embedding",
        metadata_columns: Optional[list[str]] = None,
        id_column: str = "langchain_id",
        metadata_json_column: Optional[str] = "langchain_metadata",
        distance_strategy: DistanceStrategy = DEFAULT_DISTANCE_STRATEGY,
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        index_query_options: Optional[QueryOptions] = None,
        hybrid_search_config: Optional[HybridSearchConfig] = None,
    ) -> None:
        super().__init__(
            key=key,
            engine=engine,
            embedding_service=embedding_service,
            table_name=table_name,
            schema_name=schema_name,
            content_column=content_column,
            embedding_column=embedding_column,
            metadata_columns=metadata_columns,
            id_column=id_column,
            metadata_json_column=metadata_json_column,
            distance_strategy=distance_strategy,
            k=k,
            fetch_k=fetch_k,
            lambda_mult=lambda_mult,
            index_query_options=index_query_options,
            hybrid_search_config=hybrid_search_config,
        )
    
    
