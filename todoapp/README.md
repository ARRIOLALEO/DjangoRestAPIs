# this is the TODOAP Django Backend and React FrontEnd

this app is develop to practice the basic creation os RestApp with a react backend
in order to provide an undestanding of the best practices

## basic structure


```bash
.
├── Backend
│   └── django.py
├── frontEnd
│   └── react.js
└── README.md
```
### install the virtual env for our backe end 

- pipenv install django

 in order to run our virtual environment we need to run the command 
 
- pipenv shell

now we have to see (backend)$ .. here is your root now we are alredy in our environment

now we have installed our Django nexts steps are:

- django-admin startproject config
- python manage.py startapp todos
- python manage.py  migrate

first we create a new project, and we add a new application that is our todos and to the end
we called migrate that create all the tables with this command we run all the SQL queries by defaul
django will install SQLite 

### the instaltion of rest_framework is needed

-pipenv install djangorestframework


