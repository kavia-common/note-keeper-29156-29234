# Notes Backend (Django)

This is the Django REST API for the Notes application. It provides endpoints to create, list, update, and delete notes and includes a health check and API documentation.

## Features
- Django REST Framework for API endpoints
- Swagger/Redoc docs at /docs and /redoc
- Environment-driven configuration for DEBUG, SECRET_KEY, and database
- SQLite default for local development, Postgres support for production

## Requirements
- Python 3.11+ (compatible with Django 5.2 per requirements.txt)
- pip
- Optional: Postgres database server (if not using SQLite)

## Environment Configuration

Configuration is controlled via environment variables. Copy the included example file and adjust:

```
cp .env.example .env
```

Then edit `.env` as needed.

Supported variables:
- DEBUG: set to false in production (e.g., DEBUG=false)
- SECRET_KEY: set a strong secret for production
- DATABASE_URL: a single URL for database configuration (recommended)
  - Postgres: postgres://user:password@host:5432/dbname
  - SQLite: sqlite:///absolute/path/to/db.sqlite3 or sqlite:///:memory:
- POSTGRES_*: Discrete variables used only if DATABASE_URL is not set
  - POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT

Precedence:
1) If DATABASE_URL is set, it is used.
2) Else, if POSTGRES_DB, POSTGRES_USER, and POSTGRES_HOST are set, a Postgres connection is used.
3) Else, defaults to SQLite at BASE_DIR/db.sqlite3.

Note: No third-party env parsing library is used. Values are read via os.environ.

## Running Locally

1) Create and activate a virtual environment (recommended):
```
python -m venv .venv
. ./.venv/bin/activate
```

2) Install dependencies:
```
pip install -r requirements.txt
```

3) Configure environment:
- Copy .env.example to .env and set values as desired.
- For SQLite (default), you can omit database-related variables.

4) Apply migrations:
```
python manage.py migrate
```

5) Run the server:
```
python manage.py runserver 0.0.0.0:8000
```

6) Access:
- Health: http://localhost:8000/api/health/
- Notes API: http://localhost:8000/api/notes/
- Swagger Docs: http://localhost:8000/docs/
- Redoc: http://localhost:8000/redoc/

## Switching Between SQLite and Postgres

- SQLite (default):
  - Do nothing; the app uses BASE_DIR/db.sqlite3 automatically.
  - Or explicitly set DATABASE_URL to a sqlite URL (e.g., sqlite:///absolute/path/to/db.sqlite3).

- Postgres:
  - Option A (recommended): Set DATABASE_URL, for example:
    ```
    DATABASE_URL=postgres://user:password@notes_database:5432/notes
    ```
  - Option B: Set discrete vars (used only if DATABASE_URL is not set):
    ```
    POSTGRES_DB=notes
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_HOST=notes_database
    POSTGRES_PORT=5432
    ```

After changing database configuration, run migrations again:
```
python manage.py migrate
```

## Migrations and Admin

- Create migrations (when you change models):
```
python manage.py makemigrations
python manage.py migrate
```

- Create a superuser (optional, for admin):
```
python manage.py createsuperuser
```
Admin is available at /admin.

## Notes

- ALLOWED_HOSTS and CORS are configured permissively for development. Harden for production as needed.
- Ensure SECRET_KEY and DEBUG are appropriate for production deployments.
