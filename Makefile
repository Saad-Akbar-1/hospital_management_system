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
	isort -l=120 . 

quality:
	pylint * --rcfile=.rcfile

coverage:
	coverage run --source='.' manage.py test
	coverage report
	