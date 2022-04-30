# cannot use alpine - due to an issue with pyodbc in non-windows contianer,
# the apt-get install used to fix this issue.
# Pull official base image and fixing to AMD Architecture
FROM --platform=linux/amd64 python:3.8.6

RUN apt-get update \
    && apt-get install -y curl apt-transport-https \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

COPY requirements.txt .
RUN pip install -r requirements.txt --ignore-installed

WORKDIR /app
COPY . /app

CMD gunicorn -w 4 app:app -b :8000