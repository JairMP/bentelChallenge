start:
	python manage.py runserver
tests:
	pytest
migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate 
setup:
	pip install -r requirements.txt