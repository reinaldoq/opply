SHELL := /bin/bash

build:
	docker-compose build --no-cache

up:
	docker-compose up

makemigrations:
	docker-compose run app python manage.py makemigrations

migrate:
	docker-compose run app python manage.py migrate

bash-docker:
	docker-compose exec app bash

createsuperuser:
	docker-compose run app python manage.py createsuperuser

shell:
	docker-compose run app python manage.py shell

testing:
	docker-compose run app python -m pytest -c pytest.ini --cov


