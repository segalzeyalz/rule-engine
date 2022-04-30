import logging

from managers.query_manager import QueryManager


class QueryManagerFactory:
    query_manager_cache = {}

    @classmethod
    def create(cls, table: str):
        if table in cls.query_manager_cache:
            logging.debug(f"Create a table: {table}")
            return cls.query_manager_cache[table]
        logging.debug(f"Create a table: {table}")
        cls.query_manager_cache[table] = QueryManager(table)
        logging.debug(f"{table} was created")
        return QueryManager(table)
