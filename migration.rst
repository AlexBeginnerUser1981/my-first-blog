1. python manage.py dumpdata --exclude auth.permission --exclude contenttypes > django_data.json
2. create bd, change default in DATABASES in setting.py
3. python manage.py syncdb
4. python manage.py sqlflush | psql -U myusername mydatabase ??
5. python manage.py loaddata django_data.json
6. python manage.py sqlsequencereset appname | psql -U myusername mydatabase


