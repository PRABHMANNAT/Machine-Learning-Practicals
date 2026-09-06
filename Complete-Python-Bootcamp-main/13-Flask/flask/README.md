# Beginner Flask Learning Folder

Start with the detailed guide one level above:

- `../13.1-handbook-flask-bridge.md`
- `FLASK-CHEAT-SHEET.md`
- `PRACTICE.md`

## Recommended order

1. `app.py` — Hello World, routes, dynamic URL.
2. `main.py` — templates and multiple pages.
3. `getpost.py` — GET/POST and form validation.
4. `jinja.py` — Jinja conditions/loops and redirects.
5. `api.py` — in-memory JSON CRUD API.
6. `demos/` — practical calculator, errors, cookies, auth, SQLite, Blueprints.
7. `tests/test_flask_examples.py` — test-client examples.

## Setup

```text
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Run the checks without starting a server:

```text
python -m unittest discover -s tests -v
```

The applications are intentionally separate so each concept stays small. In a
real project, combine features through an application factory and Blueprints,
as demonstrated in `demos/blueprint_app/`.
