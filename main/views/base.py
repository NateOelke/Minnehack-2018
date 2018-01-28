from flask import Flask, Blueprint, render_template, request

blueprint = Blueprint("base", __name__)

@blueprint.route("/")
def index():
    return render_template('index.html')
