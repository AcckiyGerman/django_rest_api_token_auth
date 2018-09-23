# django rest api with token auth

This is a template django API application which uses token-based authorization.

# Setup in debian/ubuntu:

## create virtual environment
**either by python utility (sudo apt install python3-venv):**
`python3 -m venv venv`

**or you can use virtualenv (sudo apt install virtualenv):**
`virtualenv venv`

## load environment
`source venv/bin/activate`

## initialize project
```
pip install -r requirements.txt
python manage.py makemigrations basesite
python manage.py migrate
python manage.py createsuperuser
```
## run
`python manage.py runserver`

Now go to http://localhost:8000 and check the site is working (login page must to appear)
then go to http://localhost:8000/admin , log in with admin credentials and in the Django admin page you can create few users to test the chat.
