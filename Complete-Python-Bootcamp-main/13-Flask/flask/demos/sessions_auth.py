"""Authentication basics with password hashing and signed Flask sessions.

This is intentionally small, not production authentication. A real app needs a
database, unique users, CSRF protection, rate limiting, password reset, secure
transport, authorization, audit logging, and often a mature auth extension or
identity provider.
"""

from functools import wraps
import os
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


ROOT = Path(__file__).resolve().parents[1]
app = Flask(__name__, template_folder=str(ROOT / "templates"), static_folder=str(ROOT / "static"))
app.config.update(
    SECRET_KEY=os.environ.get("FLASK_SECRET_KEY", "dev-only-change-me"),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

# Store hashes, never plaintext passwords. This in-memory user is a demo only.
USERS = {"learner": generate_password_hash("flask123")}


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "username" not in session:
            flash("Please log in first.", "error")
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)
    return wrapped


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        stored_hash = USERS.get(username)
        if stored_hash and check_password_hash(stored_hash, password):
            session.clear()
            session["username"] = username
            # Do not redirect blindly to an external `next` URL (open redirect).
            target = request.args.get("next", "")
            if not target.startswith("/") or target.startswith("//"):
                target = url_for("dashboard")
            return redirect(target)
        flash("Invalid username or password.", "error")
    return render_template("login.html", page_title="Login")


@app.get("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", page_title="Dashboard", username=session["username"])


@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=5004)

