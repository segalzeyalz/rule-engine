from flask import Blueprint, request, abort
import logging

from managers.fact_manager import FactManager
from managers.query_manager_factory import QueryManagerFactory
from managers.rule_manager import RuleManager

routes = Blueprint(__name__, 'blueprint')


# TODO: Check in the route that the user's input is safe (YOU ARE TAKING IT AND EXC A QUERY ON DB - NOT SAFE!!!)
@routes.route('/facts', methods=['GET'])
def get_facts():
    # avoid circular import
    from app import query_engine_manager
    logging.info(f"params are: {request.args}")
    table_name = request.args.get("tableName")
    if not table_name:
        abort(400, "Table name was not supplied")
        logging.exception("Table name wasn't supplied")
    sql_queries = QueryManagerFactory.create(table_name)
    fact_data = FactManager(sql_queries, query_engine_manager).retrieve_facts()
    if fact_data.get("Error"):
        # Todo: more specific rules
        return fact_data, 404

    return fact_data, 200


@routes.route('/rules', methods=['GET'])
def get_rules():
    # avoid circular import
    from app import query_engine_manager
    table_name = request.args["tableName"]
    sql_queries = QueryManagerFactory.create(table_name)
    rules_status = RuleManager(query_manager=sql_queries, query_engine=query_engine_manager).retrieve_rules()
    if rules_status.get("Error"):
        # Todo: more specific status codes per issue
        return rules_status, 404
    return rules_status, 200
