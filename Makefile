run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser

test:
	python manage.py test 
requirements:
	pip install -r requirements.txt

sort:
	isort -w=120 . 

quality:
	pylint hms patient --rcfile=.rcfile

coverage:
	coverage run --source='.' manage.py test patient doctor
	coverage report
	