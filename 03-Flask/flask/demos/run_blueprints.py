"""Development entry point for the application-factory/Blueprint demo."""

try:
    from .blueprint_app import create_app
except ImportError:  # Allows `python demos/run_blueprints.py` too.
    from blueprint_app import create_app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, port=5006)
