# Setting up a Development Environment

This document details how to set up a local development environment that will
allow you to contribute changes to the project.

Acquire sources and create virtualenv.
```shell
git clone https://github.com/langchain-ai/langchain-yugabytedb
cd langchain-yugabytedb
uv venv --python=3.13
source .venv/bin/activate
```

Install package in editable mode.
```shell
uv pip install pipx  
pipx install poetry
poetry install
uv pip install pytest pytest_asyncio pytest-timeout langchain-core langchain_tests sqlalchemy psycopg numpy pgvector
```

Start YugabyteDB RF-1 Universe.
```shell
docker run -d --name yugabyte_node01 --hostname yugabyte01 \
  -p 7000:7000 -p 9000:9000 -p 15433:15433 -p 5433:5433 -p 9042:9042 \
  yugabytedb/yugabyte:2.25.2.0-b359 bin/yugabyted start --background=false \
  --master_flags="allowed_preview_flags_csv=ysql_yb_enable_advisory_locks,ysql_yb_enable_advisory_locks=true" \
  --tserver_flags="allowed_preview_flags_csv=ysql_yb_enable_advisory_locks,ysql_yb_enable_advisory_locks=true"

docker exec -it yugabyte_node01 bin/ysqlsh -h yugabyte01 -c "CREATE extension vector;"
```

Invoke test cases.
```shell
pytest -vvv tests/unit_tests/yugabytedb_tests
```
