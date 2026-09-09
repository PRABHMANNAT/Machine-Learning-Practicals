# Flask demo map

Run commands from the `flask/` folder after installing Flask:

```text
python -m pip install Flask
python demos/multi_page.py
```

| File | Main lesson |
|---|---|
| `multi_page.py` | routes, dynamic URL values, query strings, templates |
| `form_calculator.py` | GET/POST, forms, validation, redirect pattern |
| `responses_errors.py` | response objects, cookies, redirects, error handlers |
| `sessions_auth.py` | sessions, password hashing, authentication basics |
| `database_crud.py` | SQLite-backed create/read/update/delete project |
| `blueprint_app/` | application factory and blueprints |
| `../api.py` | JSON REST-style CRUD API |
| `../wsgi.py` | production server entry point |

These are teaching examples. Production applications also need CSRF protection,
secure secret management, authorization, tests, migrations, observability, and a
real deployment configuration.

