"""Demo 4: dynamic routes, Jinja2, forms, redirects, and url_for().

Jinja syntax:
    {{ expression }}   print an escaped value
    {% statement %}    if/for/include/block instructions
    {# comment #}      template-only comment
"""

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.get("/")
def welcome():
    return "<h1>Welcome to the Flask course</h1>"


@app.get("/index")
def index():
    return render_template("index.html", page_title="Jinja home")


@app.get("/about")
def about():
    return render_template("about.html", page_title="About")


@app.get("/success/<int:score>")
def success(score: int):
    result = "PASSED" if score >= 50 else "FAILED"
    return render_template("result.html", results=score, label=result)


@app.get("/successres/<float:score>")
def successres(score: float):
    result = "PASSED" if score >= 50 else "FAILED"
    details = {"score": round(score, 2), "result": result}
    return render_template("result1.html", results=details)


# Keep the original misspelled route for compatibility with old lesson links.
@app.get("/sucessif/<int:score>")
def successif(score: int):
    return render_template("result.html", results=score)


@app.get("/fail/<int:score>")
def fail(score: int):
    return render_template("result.html", results=score)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "GET":
        return render_template("getresult.html", page_title="Score calculator")

    field_names = ["science", "maths", "c", "datascience"]
    try:
        scores = [float(request.form.get(field, "")) for field in field_names]
    except ValueError:
        return render_template(
            "getresult.html",
            page_title="Score calculator",
            error="Every score must be a number.",
        ), 400

    if any(score < 0 or score > 100 for score in scores):
        return render_template(
            "getresult.html",
            page_title="Score calculator",
            error="Scores must be between 0 and 100.",
        ), 400

    average = sum(scores) / len(scores)
    return redirect(url_for("successres", score=average))


if __name__ == "__main__":
    app.run(debug=True)

