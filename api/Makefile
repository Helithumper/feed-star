.PHONY: init build run db-migrate test tox

init: build run db-migrate
	docker-compose exec web feedstar init

build:
	docker-compose build

run:
	docker-compose up -d

db-migrate:
	docker-compose exec web feedstar db migrate

test:
tox:
	docker-compose run -v $(PWD)/tests:/code/tests:ro web tox -e py37
