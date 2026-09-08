"""Demo 1: the smallest useful Flask application.

Run:
    python app.py
Then visit http://127.0.0.1:5000/ and /index.

Explain it like I am 5: Flask is a receptionist. A browser asks for a URL,
Flask finds the matching route function, and that function returns a response.
"""

from flask import Flask


# __name__ helps Flask locate this module's templates and static files.
app = Flask(__name__)


@app.get("/")
def welcome():
    """Return a tiny plain-text response for the home URL."""
    return "Welcome to this beginner-friendly Flask course!"
    # return "<html><h1>Welcome to this beginner-friendly Flask course!</h1></html>"


@app.get("/index")
def index():
    """A second route proves one app can serve many URLs."""
    return "Welcome to the index page"


@app.get("/hello/<name>")
def hello(name: str):
    """Dynamic route: Flask places the URL value into `name`."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # debug=True is convenient locally: it reloads code and shows rich errors.
    # Never expose the development debugger on a public/production server.
    app.run(debug=True)
