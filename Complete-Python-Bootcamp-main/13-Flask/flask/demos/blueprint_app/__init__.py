"""Application factory: create and configure an app when requested."""

import os
from pathlib import Path

from flask import Flask


ROOT = Path(__file__).resolve().parents[2]


def create_app(test_config=None):
    app = Flask(
        __name__,
        template_folder=str(ROOT / "templates"),
        static_folder=str(ROOT / "static"),
    )
    app.config.from_mapping(SECRET_KEY=os.environ.get("FLASK_SECRET_KEY", "dev-only-change-me"))
    if test_config:
        app.config.update(test_config)

    from .pages import pages
    from .api import api

    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix="/api")
    return app

