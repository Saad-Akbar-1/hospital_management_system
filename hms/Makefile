run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser

test:
	python manage.py test patient

requirements:
	pip install -r requirements.txt

sort:
	isort patient
	isort hms

quality:
	pylint hms patient --rcfile=.rcfile

coverage:
	coverage run --source='.' manage.py test patient
	coverage report