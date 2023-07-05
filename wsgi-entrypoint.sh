#!/bin/sh

until cd /app/
do
    echo "Waiting for server volume..."
done

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput


gunicorn Menu_For_Soulist.wsgi --bind 0.0.0.0:8080 --workers 4 --threads 4
