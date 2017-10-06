### Hi! Check out the blog post -> [Asynchronous Tasks with Django and Celery](https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery)

Run redis
```bash
redis-server
```

Run celery
```bash
celery -A picha worker -l info
```

Run django
```bash
python manage.py migrate
python manage.py runserver
```



