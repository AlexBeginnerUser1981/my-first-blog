1. static files
1.0. add to setting.py


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'quickstart', 'static'),
)

1.1. add directory static to app directory
1.2. copy to static directory from venv/lib/python3.11/site-package/django/rest-framework/static/
1.3. load to pythonanywhere thru zip
1.4. add path to dir with static on the web (path is 'home/AlexanderBegineer1981/winproject')

-----DROP ALL TABLES IN DATABASE - this is not work at all
python manage.py migrate quickstart zero

full kill all including superuser - - this is not work at all
python manage.py flush

--------PYTHONANYWHERE ADDRESS-----------------------------------
https://alexbeginneruser1981.pythonanywhere.com/winproject


get data
python manage.py dumpdata quickstart --exclude auth.permission --exclude contenttypes --indent 2 > quick.json

load data
python manage.py loaddata quick.json