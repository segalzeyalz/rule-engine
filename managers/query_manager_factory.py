from managers.query_manager import QueryManager


class QueryManagerFactory:
    query_manager_cache = {}

    @classmethod
    def create(cls, table: str):
        if table in cls.query_manager_cache:
            return cls.query_manager_cache[table]
        return QueryManager(table)
