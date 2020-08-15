# backend2

korero backend written in Python

## Installation

### Docker (testing)

You'll need `docker` and `docker-compose` installed.

Go to the project's root directory and run:

```
docker-compose up
```

You can edit the environment variables in `docker-compose.yml`.

### Standard installation (development)

If `DEBUG` is set to `true` or `1`, the backend will use the SQLite3 engine,
so you don't have to install PostgreSQL.
However, Redis will be needed in future.

Create and switch to a virtual environment (not required, but highly recommended):

```
python -m venv venv


On Linux/OSX:

source venv/bin/activate

On Windows:

.\venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Migrate database changes:

```
python3 korero/manage.py migrate
```

Create a superuser (optional):

```
python3 korero/manage.py createsuperuser
```

And finally, run the development server:

```
python3 korero/manage.py runserver
```

## Tests

### Run using docker-compose:

```
docker-compose run web bash -c "cd korero && python3 manage.py migrate && python3 manage.py test"
```

### Run using the manage.py CLI:

```
cd korero
python3 manage.py migrate
python3 manage.py test
```

### Note

_For some reason django won't discover tests if you aren't in the folder containing `manage.py`._
