#!/usr/bin/env bash

postgres_ready() {
python << END
import sys

import psycopg2

try:
    psycopg2.connect(
        dbname="test",
        user="test",
        password="123456",
        host="db",
        port="5432",
    )
except psycopg2.OperationalError as e:
    print(str(e))
    sys.exit(-1)
sys.exit(0)

END
}
until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available'

python manage.py makemigrations
python manage.py migrate

python manage.py import_data
python manage.py export_data

#python manage.py create_default_user
# python manage.py collectstatic
#python manage.py runserver 0.0.0.0:8000 & celery -A prj worker --loglevel=debug & celery -A prj beat -l debug

python manage.py runserver 0.0.0.0:8000

exec "$@"
