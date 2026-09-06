"""A small calculator demonstrating GET, POST, validation, and templates."""

from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for


ROOT = Path(__file__).resolve().parents[1]
app = Flask(__name__, template_folder=str(ROOT / "templates"), static_folder=str(ROOT / "static"))

OPERATIONS = {
    "add": ("+", lambda left, right: left + right),
    "subtract": ("−", lambda left, right: left - right),
    "multiply": ("×", lambda left, right: left * right),
    "divide": ("÷", lambda left, right: left / right),
}


@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "GET":
        return render_template("calculator.html", page_title="Calculator", operations=OPERATIONS)

    try:
        left = float(request.form.get("left", ""))
        right = float(request.form.get("right", ""))
    except ValueError:
        return render_template(
            "calculator.html",
            page_title="Calculator",
            operations=OPERATIONS,
            error="Please enter two valid numbers.",
        ), 400

    operation = request.form.get("operation", "")
    if operation not in OPERATIONS:
        return "Unknown operation", 400
    if operation == "divide" and right == 0:
        return render_template(
            "calculator.html",
            page_title="Calculator",
            operations=OPERATIONS,
            error="Division by zero is not allowed.",
        ), 400

    symbol, function = OPERATIONS[operation]
    result = function(left, right)
    # Redirect turns a POST into a bookmarkable GET result URL.
    return redirect(url_for("show_result", left=left, right=right, symbol=symbol, result=result))


@app.get("/result")
def show_result():
    return render_template("calculator_result.html", page_title="Result", values=request.args)


if __name__ == "__main__":
    app.run(debug=True, port=5002)

