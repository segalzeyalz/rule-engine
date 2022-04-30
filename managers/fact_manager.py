import logging

from sqlalchemy.exc import ProgrammingError

from managers.query_engine_manager import QueryEngineManager
from managers.query_manager import QueryManager


class FactManager:
    def __init__(self, query_manager: QueryManager, query_engine: QueryEngineManager):
        self.query_manager = query_manager
        self.query_engine = query_engine

    def retrieve_facts(self):
        fact_data = {}
        for sql_query in self.query_manager:
            query = sql_query.query
            query_name = sql_query.name
            try:
                fact_data[query_name] = self.query_engine.execute_query(query)
            except ProgrammingError as e:
                # TODO: the engine should get that data
                # Todo: mention which table
                if "Invalid object name" in str(e):
                    fact_data["error"] = "this table is not exist"
                    logging.exception("this table is not exist")
                else:
                    fact_data["Error"] = str(e)
                    logging.exception(str(e))
                break
            except Exception as e:
                fact_data["error"] = str(e)
                logging.exception(str(e))
                break

        return fact_data
