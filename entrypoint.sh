#!/bin/sh
echo "Running Django Entrypoint commands"
export NEW_RELIC_CONFIG_FILE=newrelic.ini

RETRIES=5

until psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c "select 1" > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
  echo "Waiting for postgres server to start, $((RETRIES)) remaining attempts..."   RETRIES=$((RETRIES-=1))
  sleep 1
done

echo "Creating migrations, if any..."
python manage.py makemigrations

echo "Running new migrations, if any..."
python manage.py migrate

echo "Collecting staticfiles"
python manage.py collectstatic

echo "Initializing Database, then loading data"
python initialize_db.py

newrelic-admin run-program gunicorn newrelic_python_kata.wsgi
