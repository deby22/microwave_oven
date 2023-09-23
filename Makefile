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

test:  ## Run unit tests
	cd api && python -m pytest tests -m "not integration" && cd ..


integration:  ## Run integration tests
	cd api && python -m pytest tests -m integration && cd ..