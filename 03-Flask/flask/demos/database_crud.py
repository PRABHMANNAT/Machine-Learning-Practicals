"""A complete tiny CRUD project using Flask, Jinja, and SQLite."""

from pathlib import Path
import sqlite3

from flask import Flask, abort, g, redirect, render_template, request, url_for


ROOT = Path(__file__).resolve().parents[1]


def create_app(test_config=None):
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder=str(ROOT / "templates"),
        static_folder=str(ROOT / "static"),
    )
    app.config.from_mapping(DATABASE=str(Path(app.instance_path) / "crud.sqlite3"))
    if test_config:
        app.config.update(test_config)
    # Create the folder that will contain the configured database. Tests can
    # point this at a temporary directory instead of touching app data.
    Path(app.config["DATABASE"]).parent.mkdir(parents=True, exist_ok=True)

    def get_db():
        if "db" not in g:
            g.db = sqlite3.connect(app.config["DATABASE"])
            g.db.row_factory = sqlite3.Row
        return g.db

    @app.teardown_appcontext
    def close_db(error=None):
        database = g.pop("db", None)
        if database is not None:
            database.close()

    def init_db():
        database = get_db()
        database.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0 CHECK (done IN (0, 1))
            )
        ''')
        database.commit()

    def get_task(task_id):
        task = get_db().execute("SELECT id, title, done FROM tasks WHERE id = ?", (task_id,)).fetchone()
        if task is None:
            abort(404)
        return task

    @app.get("/")
    def index():
        tasks = get_db().execute("SELECT id, title, done FROM tasks ORDER BY id DESC").fetchall()
        return render_template("items.html", page_title="Task CRUD", tasks=tasks)

    @app.route("/create", methods=["GET", "POST"])
    def create():
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            if not title:
                return render_template("item_form.html", page_title="New task", error="Title is required"), 400
            database = get_db()
            database.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
            database.commit()
            return redirect(url_for("index"))
        return render_template("item_form.html", page_title="New task")

    @app.route("/edit/<int:task_id>", methods=["GET", "POST"])
    def edit(task_id):
        task = get_task(task_id)
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            if not title:
                return render_template("item_form.html", page_title="Edit task", task=task, error="Title is required"), 400
            done = 1 if request.form.get("done") == "on" else 0
            database = get_db()
            database.execute("UPDATE tasks SET title = ?, done = ? WHERE id = ?", (title, done, task_id))
            database.commit()
            return redirect(url_for("index"))
        return render_template("item_form.html", page_title="Edit task", task=task)

    @app.post("/delete/<int:task_id>")
    def delete(task_id):
        get_task(task_id)
        database = get_db()
        database.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        database.commit()
        return redirect(url_for("index"))

    app.get_db = get_db
    app.init_db = init_db
    with app.app_context():
        init_db()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5005)
