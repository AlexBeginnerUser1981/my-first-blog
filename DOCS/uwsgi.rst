https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
https://www.8host.com/blog/nastrojka-uwsgi-i-nginx-dlya-obsluzhivaniya-prilozhenij-python-v-ubuntu-14-04/
1. pip install uwsgi
2. create uwsgi.ini file
3. uwsgi /Users/kochnev/PycharmProjects/DjangoRest/winproject/uwsgi.ini
4. ps aux | grep uwsgi  # run in terminal to see processes active
5. create upstart file (ommited)
6.