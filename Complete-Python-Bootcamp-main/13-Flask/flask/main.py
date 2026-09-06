"""Demo 2: render HTML templates for a small multi-page site."""

from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def welcome():
    # Returning HTML directly works, but templates are cleaner for real pages.
    return "<h1>Welcome to the Flask course</h1>"


@app.get("/index")
def index():
    return render_template(
        "index.html",
        page_title="Home",
        message="This page came from a Jinja template.",
    )


@app.get("/about")
def about():
    return render_template("about.html", page_title="About")


if __name__ == "__main__":
    app.run(debug=True)
