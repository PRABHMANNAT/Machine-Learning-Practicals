"""HTML routes grouped in a Blueprint."""

from flask import Blueprint, render_template


pages = Blueprint("pages", __name__)


@pages.get("/")
def home():
    return render_template("blueprint_home.html", page_title="Blueprint demo")


@pages.get("/about")
def about():
    return render_template("about.html", page_title="Blueprint about")

