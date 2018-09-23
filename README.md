# Django REST API with Token authorization template.

This is a template django API application which uses token-based authorization.

# Setup in debian/ubuntu:

## create virtual environment

either by python utility (sudo apt install python3-venv):

`python3 -m venv venv`

or you can use virtualenv (sudo apt install virtualenv):

`virtualenv venv`

## load environment

`source venv/bin/activate`

## initialize project

```
pip install -r requirements.txt
python manage.py makemigrations users
python manage.py migrate
python manage.py createsuperuser
```
## run

`python manage.py runserver`

Go to http://localhost:8000/admin , log in with admin credentials and 
create few users for testing.

Go to http://localhost:8000/users to test the API.
All necessary information is provided on the page.
