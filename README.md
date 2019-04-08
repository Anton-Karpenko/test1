## Installation 
1. `python -m venv .venv` 
2. `source .venv/bin/activate`
3. `pip install -r requirements/local.txt`
4. Create `.env` file and add some variables:
    ```
    REDIS_URL=redis://redis:6379/0
    DATABASE_URL=postgres://<user>:<pass>@localhost:5432/<db_name>
    CELERY_BROKER_URL=redis://redis:6379/0
    ```
5. `make migrate`
6. Create `static` dir in root directory
7. `make superuser`
8. `make server`

### Links
[Swagger documentation](http://127.0.0.1:8000/swagger)

[Admin panel](http://127.0.0.1:8000/admin)

### Make file
```
coverage:
	coverage run -m pytest
coverage-report:
	coverage report -m
server:
	python manage.py runserver
migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations
superuser:
	python manage.py createsuperuser
```

## Possible improvements 
Because of limited time this project lacks:
1. Documentation
2. Unit-tests (There are only couple for images app)
3. Views count for items can be stored in cache to unload primary db