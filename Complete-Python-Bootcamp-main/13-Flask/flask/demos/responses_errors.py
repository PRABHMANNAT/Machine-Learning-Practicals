"""Response objects, redirects, cookies, and HTML/JSON error handlers."""

from pathlib import Path

from flask import Flask, jsonify, make_response, redirect, render_template, request, url_for


ROOT = Path(__file__).resolve().parents[1]
app = Flask(__name__, template_folder=str(ROOT / "templates"), static_folder=str(ROOT / "static"))


@app.get("/")
def index():
    return render_template("error_demo.html", page_title="Responses and errors")


@app.get("/old-home")
def old_home():
    return redirect(url_for("index"), code=302)


@app.get("/set-theme/<theme>")
def set_theme(theme: str):
    if theme not in {"light", "dark"}:
        return "Theme must be light or dark", 400
    response = make_response(redirect(url_for("index")))
    response.set_cookie(
        "theme",
        theme,
        max_age=60 * 60 * 24 * 30,
        httponly=True,
        samesite="Lax",
        secure=not app.debug,
    )
    return response


@app.get("/api/problem")
def api_problem():
    return jsonify({"error": "Demonstration conflict"}), 409


@app.get("/boom")
def boom():
    raise RuntimeError("Intentional teaching error")


@app.errorhandler(404)
def not_found(error):
    if request.path.startswith("/api/"):
        return jsonify({"error": "Not found"}), 404
    return render_template("404.html", page_title="Not found"), 404


@app.errorhandler(500)
def internal_error(error):
    # Log the original exception on a real application boundary.
    app.logger.error("Unhandled request error", exc_info=error.original_exception)
    return render_template("500.html", page_title="Server error"), 500


if __name__ == "__main__":
    app.run(debug=True, port=5003)

