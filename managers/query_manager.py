from dataclasses import dataclass

from sqlalchemy import text


@dataclass
class Query:
    name: str
    query: any


class QueryManager:
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.queries = [
            Query(name="number of rows", query=self.number_of_rows(table_name)),
            Query(name="number of indexes", query=self.number_of_indexes(table_name)),
            Query(name="has primary key", query=self.has_primary_key(table_name)),
            Query(name="primary key count columns", query=self.primary_key_count_columns(table_name))
        ]

    @staticmethod
    def number_of_rows(table_name: str):
        query = f"SELECT count(*) FROM {table_name}"
        return text(query)

    @staticmethod
    def number_of_indexes(table_name: str):
        query = f""" SELECT count(*)
    FROM sys.indexes AS IND
    WHERE object_id = object_ID('${table_name}')
    AND index_id != 0"""
        return text(query)

    @staticmethod
    def has_primary_key(table_name: str):
        query = f"""
    SELECT CASE
        WHEN Count(index_id) = 1 THEN 'true'
        Else 'false'
        END
    FROM sys.indexes
    WHERE object_id = object_id('${table_name}')"""
        return text(query)

    @staticmethod
    def primary_key_count_columns(table_name: str):
        query = f"""
    SELECT COUNT(INC.column_id)
    FROM sys.indexes as IND
        INNER JOIN sys.index_columns as INC
            ON IND.object_id = INC.object_id
            AND IND.index_id = INC.index_id
    WHERE IND.object_id = object_id('{table_name}')
        AND IND.is_primary_key = 1;"""
        return text(query)

    def __iter__(self):
        self.n = 0
        return iter(self.queries)

    def __next__(self):
        if self.n == len(self.queries):
            raise StopIteration
        res = self.queries[self.n],
        self.n += 1
        return res
