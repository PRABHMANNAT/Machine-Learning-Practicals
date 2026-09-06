"""Production server entry point.

Example (after installing Waitress):
    waitress-serve --call wsgi:create_app

Do not use Flask's development server for production traffic.
"""

from demos.blueprint_app import create_app


app = create_app()

