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
create-dummy-data: 
ifdef $(TOTAL)
	python manage.py create_dummy_doctors --total $(TOTAL)
	python manage.py create_dummy_patients --total $(TOTAL)
	python manage.py create_dummy_reports --total $(TOTAL)
else
	python manage.py create_dummy_doctors
	python manage.py create_dummy_patients
	python manage.py create_dummy_reports
endif
delete-dummy-data:
	python manage.py delete_dummy_doctors
	python manage.py delete_dummy_patients
	python manage.py delete_dummy_reports
	