import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = "Server=metisdb1.database.windows.net;Database=ORM;UserId=user1;Password=Trustno1;"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
