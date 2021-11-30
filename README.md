# backend

## Run this commands to start project

### creat env
> python3 -m venv env
>
> source env/bin/activate
>
### install requarements
> pip install -r requarement.txt
>
### create postgres database
> pasql -U postgres
>
> create database dname;
>
> create user duser;
>
> grant all on database dname to duser;
>
> \password duser
>
### fill .env file based on .env.tempalte
### migrate
> python manage.py migrate
>
### create admin user
> python manage.py createsuperuser
>
### run
> python manage.py runserver
>