## To Start

In the command line, run

```shell
psql -f bikeshed_init.sql
```

this creates the database, the user and assigns the user to the database.

Then, to create the schema from Django's models:
inside this repo (with djangoenv running), run:

```shell
python manage.py makemigrations
python manage.py migrate
```

To initiate some mock data run

```shell
psql -d bikeshed -a -f provision_bikeshed.sql
```

Finally to start the app, run

```shell
python manage.py runserver
```

and naviagte to the URL shown in the commandline.

To add a superuser, in order to manage brands and bikes, run

```shell
python manage.py createsuperuser
```

and enter a username, email address and password, admin is found at
host:port/admin.
