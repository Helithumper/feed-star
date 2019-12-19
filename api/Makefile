.PHONY: init build run db-migrate test tox tag push default

VERSION := $(shell grep "VERSION" ./feedstar/config.py | cut -d '"' -f2)
GIT_COMMIT=$(shell git rev-parse --short HEAD)
GIT_DIRTY=$(shell test -n "`git status --porcelain`" && echo "+CHANGES" || true)
BUILD_DATE=$(shell date '+%Y-%m-%d-%H:%M:%S')
IMAGE_NAME := "helithumper/feedstar-api"

default: build test

init: build run db-migrate
	docker-compose exec web feedstar init

build:
	docker build . -t $(IMAGE_NAME):local

run:
	docker-compose up -d

db-migrate:
	docker-compose exec web feedstar db migrate

tag: build
	@echo "Tagging: latest ${VERSION} $(GIT_COMMIT)"
	docker tag $(IMAGE_NAME):local $(IMAGE_NAME):$(GIT_COMMIT)
	docker tag $(IMAGE_NAME):local $(IMAGE_NAME):${VERSION}
	docker tag $(IMAGE_NAME):local $(IMAGE_NAME):latest

push: build tag
	@echo "Pushing docker image to registry: latest ${VERSION} $(GIT_COMMIT)"
	docker push $(IMAGE_NAME):$(GIT_COMMIT)
	docker push $(IMAGE_NAME):${VERSION}
	docker push $(IMAGE_NAME):latest

test:
tox:
	docker-compose run -v $(PWD)/tests:/code/tests:ro web tox -e py37
