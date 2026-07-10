install:
	uv pip install --upgrade pip
	uv pip install black

build:
	uv python -m build

publish:
	uv twine upload dist/*

run:
	bash run.sh

greet:
	uv run main.py

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose down
	docker compose up -d

web:
	open http://localhost:8080

