build:
	docker compose build

load-initial-data:
	docker compose run --rm usersnacks-api python manage.py makesuperuser
	docker compose run --rm usersnacks-api python manage.py load_seed_data

# Django Commands
manage-python:
	docker compose run --rm usersnacks-api python manage.py $(command)

makemigrations-python: command=makemigrations
makemigrations-python: manage-python
mm: makemigrations-python

migrate-python: command=migrate
migrate-python: manage-python

# Server Commands
run-server:
	docker compose up --no-log-prefix usersnacks-api

run-celery:
	docker compose up --no-log-prefix usersnacks-celery

run-databases:
	docker compose up --no-log-prefix postgres-database redis-database

run-redis:
	docker compose up --no-log-prefix redis-database

run-commander:
	docker compose up --no-log-prefix redis-commander

run-shell:
	docker compose run --rm usersnacks-api python manage.py shell
