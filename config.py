import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # TODO: IN Readme - say that the env vars are currently in the docerfile, but in real prod would be fetched from secret manager etc.
    USERID = os.getenv("USER_ID")
    PWD = os.getenv("PWD")
    _params = urllib.parse.quote_plus(
        r'Driver={ODBC Driver 17 for SQL Server};Server=tcp:metisdb1.database.windows.net,1433;'
        r'Database=ORM;Uid=<<UID>>@metisdb1;Pwd=<<PWD>>;'
        r'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=300;'
            .replace("<<UID>>", USERID)
            .replace("<<PWD>>", PWD))
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(_params)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
