from flask import Flask, Blueprint, render_template, request

blueprint = Blueprint("base", __name__)

@blueprint.route("/result.html", methods=["GET"])
def result():
    #with open("", "w+") as csvfile:

    return "Result"


@blueprint.route("/")
def index():
    return render_template('index.html')
