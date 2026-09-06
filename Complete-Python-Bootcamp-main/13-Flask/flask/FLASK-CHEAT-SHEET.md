# Flask Quick Revision Cheat Sheet

## Minimal app

```python
from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Hello"
```

## Most-used imports

```python
from flask import (
    Flask, abort, flash, g, jsonify, redirect,
    render_template, request, session, url_for,
)
```

## Request data

```python
request.method
request.args.get("q", "")             # ?q=...
request.form.get("name", "")          # HTML form
request.get_json(silent=True)          # JSON body
request.files.get("photo")             # upload
request.cookies.get("theme")           # cookie
```

## Responses

```python
return "OK"
return {"status": "ok"}
return jsonify(items=items), 200
return render_template("page.html", items=items)
return redirect(url_for("home"))
return "Bad input", 400
abort(404)
```

## Routes

```python
@app.get("/users/<int:user_id>")
def user(user_id): ...

@app.route("/form", methods=["GET", "POST"])
def form(): ...
```

## Jinja

```jinja2
{{ value }}
{{ name|title }}
{% if ready %}...{% endif %}
{% for item in items %}...{% endfor %}
{% extends "base.html" %}
{% block content %}...{% endblock %}
```

## JSON CRUD pattern

| Action | Method + route | Success |
|---|---|---:|
| List | `GET /items` | 200 |
| Retrieve | `GET /items/1` | 200 |
| Create | `POST /items` | 201 |
| Update | `PUT/PATCH /items/1` | 200 |
| Delete | `DELETE /items/1` | 204 |

## Security reminders

- Debugger off in production.
- Strong secret from environment/secret manager.
- HTTPS; secure/HTTP-only/SameSite cookies.
- CSRF protection for state-changing browser forms.
- Validate and limit all input/uploads.
- Parameterize SQL values.
- Hash passwords; check authorization on every protected action.
- Escape output; never log secrets.

## Test client

```python
app.config.update(TESTING=True)
client = app.test_client()
response = client.get("/")
assert response.status_code == 200
```

## Deployment

```text
waitress-serve --call wsgi:create_app
```

Use a production WSGI server, external configuration, persistent data, logging,
monitoring, backups, and repeatable dependency installation.

