.PHONY: homework-i-run
homework-i-run:
	@python manage.py runserver

.PHONY: init-dev
init-dev:
	@python -m pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	python manage.py createsuperuser_custom

.PHONY: pre-commit-run
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
pre-commit-run-all:
	@pre-commit run --all-files
