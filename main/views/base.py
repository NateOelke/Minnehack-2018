from flask import Blueprint, render_template

blueprint = Blueprint("base", __name__)


@blueprint.route("/")
def index():
    render_template("index.html")