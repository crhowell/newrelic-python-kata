FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV NEW_RELIC_CONFIG_FILE newrelic.ini

ENV GUNICORN_CMD_ARGS "--bind=0.0.0.0:8000 --workers=3 --reload"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
