from sqlalchemy.exc import ProgrammingError

from app import app

from flask import request, jsonify
from sqlalchemy import create_engine
import urllib

from query_manager import QueryManger



@app.route('/facts', methods=['GET'])
def get_facts():
    req_args = request.args
    fact_data = {}
    sql_queries = QueryManger(table_name=req_args["tableName"])
    for sql_query in sql_queries:
        query = sql_query.get("query")
        query_name = sql_query.get("name")
        try:
            fact_data[query_name] = [res for res in azure_engine.execute(query)][0][0]
        except ProgrammingError as e:
            fact_data["error"] = str(e)
            break
    return fact_data


@app.route('/rules', methods=['GET'])
def get_rules():
    req_args = request.args
    table_name = req_args["tableName"]
    sql_queries = QueryManger(table_name=table_name)
    rules_status = {}
    for query_item in sql_queries:
        query_name = query_item.get("name")
        query = query_item.get("query")
        query_res = [res for res in azure_engine.execute(query)][0][0]
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
        if rule_name:
            rules_status[rule_name] = message

    return rules_status
