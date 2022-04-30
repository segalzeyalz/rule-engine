from flask import Flask
from sqlalchemy import create_engine

from managers.query_engine_manager import QueryEngineManager
from router import routes
from config import Config
import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT)

app = Flask(__name__)
app.config.from_object(Config)
azure_engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=True)
query_engine_manager = QueryEngineManager(azure_engine)
app.register_blueprint(routes)
