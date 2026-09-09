"""Demo 3: GET, POST, forms, validation, and Post/Redirect/Get."""

from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
# Flash messages use the signed session cookie. Use an environment secret in a
# real deployment; this fixed value is only for a local learning demo.
app.config["SECRET_KEY"] = "dev-only-change-me"


@app.get("/")
def welcome():
    return "<h1>Welcome to the Flask course</h1>"


@app.get("/index")
def index():
    return render_template("index.html", page_title="Home")


@app.get("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/form", methods=["GET", "POST"])
def form():
    """GET shows the form; POST validates submitted form data."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            flash("Please enter your name.", "error")
            return render_template("form.html", page_title="Name form"), 400
        flash(f"Hello {name}!", "success")
        # Redirect prevents a browser refresh from submitting the form again.
        return redirect(url_for("form"))
    return render_template("form.html", page_title="Name form")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    """Preserve the original /submit example with safer input handling."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            return "Name is required", 400
        return f"Hello {name}!"
    return render_template("form.html", page_title="Submit")


if __name__ == "__main__":
    app.run(debug=True)
