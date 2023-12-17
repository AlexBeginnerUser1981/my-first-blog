https://blog.back4app.com/how-to-build-and-deploy-a-python-application/
gunicorn server setup:
1. pip install gunicorn
3. python manage.py collectstatic
4. gunicorn winproject.wsgi (run gunicorn)
5. https://docs.gunicorn.org/en/stable/settings.html#config
6. make gunicorn.conf.py
7. guncorn #run server
8. install supervisor app fro process monitiring
   pip install supervisor
9. echo_supervisord_conf > supervisord_conf
10.