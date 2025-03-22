# Description: Makefile for Django project
migrate:
	docker-compose exec web python manage.py makemigrations
	docker-compose exec web python manage.py migrate_schemas
	docker-compose exec web python manage.py migrate

setup:
	docker-compose up -d --build
	docker-compose exec web python manage.py collectstatic
	docker-compose exec web python manage.py createsuperuser
	# docker-compose exec web python manage.py create_tenant
	make migrate

run:
	docker-compose up -d --build

stop:
	docker-compose down

restart:stop run

shell:
	docker-compose exec web bash

clean: stop
	docker-compose rm
	docker container prune

deep-clean: clean
	docker image prune
	docker volume prune

logs:
	docker logs django_tenants_web