from sqlalchemy.exc import ProgrammingError


class QueryEngineManager:
    def __init__(self, engine):
        self.engine = engine

    def execute_query(self, query):
        try:
            query_res = [res for res in self.engine.execute(query)][0][0]
            return query_res
        except ProgrammingError as e:
            # Todo: mention which table
            if "Invalid object name" in str(e):
                message = "this table is not exist"
                raise ValueError(message)
            else:
                raise e
