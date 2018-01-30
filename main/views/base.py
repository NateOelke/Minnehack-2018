import sys
import numpy as np
from flask import Flask, Blueprint, render_template, request
sys.path.insert(0, "src")
from injury_model import *
sys.path.insert(0, "main")
from __init__ import *

blueprint = Blueprint("base", __name__)

@blueprint.route("/result.html", methods=["GET"])
def result():
    # Use global model created in __init__.py
    global model

    # Append submited data to database.csv
    with open("data/database.csv", "a") as csvfile:
        # Parse website form data and append as a row to the csv file
        row = ""
        args = request.args
        for key, value in args.items():
            if key == "sex":
                if value == "male":
                    row += "1,0,0,"
                elif value == "female":
                    row += "0,1,0,"
                else:
                    row += "0,0,1,"

            elif key == "position":
                #row += value + ","
                pass

            elif key == "equipment":
                if value == "free-weights":
                    row += "1,0,0,0,"
                elif value == "machines":
                    row += "0,1,0,0,"
                elif value == "both-equipment":
                    row += "0,0,1,0,"
                else:
                    row += "0,0,0,0,"

            elif value == "":
                row += "0,"

            else:
                row += value + ","

        row = row[:-1]
        row += "\n"
        csvfile.write(row)

    # Predict the number of missed games using the inputed data
    X,y = load_data("data/database.csv")
    predicted_missed_games = max(model.predict(X[-1])[0], 0)
    return render_template("result.html", predicted_missed_games=predicted_missed_games)

@blueprint.route("/")
def index():
    return render_template('index.html')
