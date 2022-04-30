import logging

from sqlalchemy.exc import ProgrammingError


class QueryEngineManager:
    def __init__(self, engine):
        self.engine = engine

    def execute_query(self, query):
        try:
            logging.info(f"execute query: {query}")
            query_res = [res for res in self.engine.execute(query)][0][0]
            logging.info(f"Query execution succeeded")
            return query_res
        except ProgrammingError as e:
            # Todo: mention which table
            if "Invalid object name" in str(e):
                message = "this table is not exist"
                logging.exception("Query execution failed")
                raise ValueError(message)
            else:
                logging.exception(e)
                raise e
