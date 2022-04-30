# cannot use alpine - due to an issue with pyodbc in non-windows contianer,
# the apt-get install used to fix this issue.
FROM python:3.7

RUN echo "[ODBC Driver 17 for SQL Server] \
Description=Microsoft ODBC Driver 17 for SQL Server \
Driver=/usr/local/lib/libmsodbcsql.17.dylib \
UsageCount=1" >/usr/local/etc/odbcinst.ini

RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev\
    unixodbc

COPY requirements.txt .
RUN pip install -r requirements.txt --ignore-installed

WORKDIR /app
COPY . /app

CMD gunicorn -w 4 app:app -b :8000
