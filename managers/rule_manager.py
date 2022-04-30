import logging
from typing import Tuple

from managers.query_engine_manager import QueryEngineManager
from managers.query_manager import QueryManager, Query

FAIL = "FAIL"
class RuleManager:
    def __init__(self, query_manager: QueryManager, query_engine: QueryEngineManager):
        self.query_manager = query_manager
        self.query_engine = query_engine

    def retrieve_rules(self) -> dict:
        rules_status = {}
        for query_item in self.query_manager:
            rule_name, msg = self._get_rule_msg(query_item)
            if rule_name and rule_name != FAIL:
                rules_status[rule_name] = msg
            else:
                return {"Error": msg}
        return rules_status

    def _get_rule_msg(self, query_item: Query) -> Tuple[str, str]:
        # TODO: ADD ALL STRINGS TO AN ENUM / DICT and iterate nicely
        query_name = query_item.name
        query = query_item.query
        try:
            query_res = self.query_engine.execute_query(query)
        except Exception as e:
            logging.exception(e)
            return FAIL, str(e)
        rule_name, message = "", "Passed"
        if query_name == "number of rows":
            rule_name = "high number of rows"
            if query_res > 10000000:
                message = f"Warning! Large table. The number of rows is {query_res}"
        elif query_name == "has primary key":
            rule_name = "no Primary Key"
            if query_res == 'false':
                message = "Warning: the table doesn’t have a PK."
        elif query_name == "primary key count columns":
            rule_name = "a Primary Key with many columns"
            if query_res >= 4:
                message = f"High number of columns in the PK: {query_res}"
        return rule_name, message
