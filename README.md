## To Start

In the command line, run

```shell
psql -f bikeshed_init.sql
```

this creates the database, the user and assigns the user to the database.

Then, to create the schema from Django's models:
inside this repo (in a djangoenv running), run:

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
