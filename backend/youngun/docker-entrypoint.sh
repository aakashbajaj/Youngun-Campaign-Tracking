# rm *.sqlite3
cd youngun

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --noinput

nohup python manage.py qcluster &
python manage.py runserver 0.0.0.0:8000