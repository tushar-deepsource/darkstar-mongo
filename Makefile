.PHONY: help clean dev docs package test

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo "	 dev 	install all deps for dev env"
	@echo "  clean	clean runtime environment"
	@echo "	 test	run all tests with coverage"
	@echo "	 image	build docker image"
	@echo "	 deploy	deploy service as a docker image container"

clean:
	rm -rf dist/*

dev:
	pip install -r requirements.txt
	pip install pytest pytest-cov flake8
	cd src
	uvicorn app.main:app --reload --host 0.0.0.0
	cd ..

image:
	docker build -t vap-heimdall-api .

test:
	flake8 src/app  --ignore F401,F403
	pytest -v --cov=./ --cov-report=xml:/tmp/coverage.xml

build:
	@echo "Deploying Heimdall API in Docker Cointainer."
	docker build -t heimdall_api_image .

deploy:
	docker run --env-file .env  --name heimdall_api -p 8090:8080 -d heimdall_api_image
	sleep 5
	docker update --restart=always heimdall_api

run:
	docker run --env-file .env  --name heimdall_api -p 8090:8080 heimdall_api_image

stop:
	docker stop heimdall_api

docker-clean:
	docker rm heimdall_api
	docker rmi heimdall_api_image
