"""Routes, dynamic routes, query strings, and template rendering."""

from pathlib import Path

from flask import Flask, render_template, request


ROOT = Path(__file__).resolve().parents[1]
app = Flask(
    __name__,
    template_folder=str(ROOT / "templates"),
    static_folder=str(ROOT / "static"),
)


@app.get("/")
def home():
    return render_template(
        "home.html",
        page_title="Multi-page demo",
        features=["routes", "templates", "query strings"],
    )


@app.get("/about")
def about():
    return render_template("about.html", page_title="About the demo")


@app.get("/hello/<name>")
def hello(name: str):
    # Converter example: /orders/not-a-number will not match this route.
    language = request.args.get("language", "English")
    return render_template(
        "greeting.html",
        page_title="Greeting",
        name=name,
        language=language,
    )


@app.get("/orders/<int:order_id>")
def order(order_id: int):
    return {"order_id": order_id, "message": "Integer converter worked"}


if __name__ == "__main__":
    app.run(debug=True, port=5001)

