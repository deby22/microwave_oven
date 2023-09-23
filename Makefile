up:  ## Run Docker Compose services
	docker-compose up -d

down:  ## Shutdown Docker Compose services
	docker-compose down

black:
	black api

flake8:
	flake8 api

isort:
	isort api

lint: isort black flake8

test:  ## Run tests
	$(PYTHON) -m pytest api 