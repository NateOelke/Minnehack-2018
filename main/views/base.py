from flask import Flask, Blueprint, render_template, request

blueprint = Blueprint("base", __name__)

@blueprint.route("/result.html", methods=["GET"])
def result():
    with open("data/database.csv", "a") as csvfile:
        row = ""
        args = request.args
        print(args)
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

        row += "\n"
        csvfile.write(row)
        return render_template("result.html", predicted_missed_games=5)


@blueprint.route("/")
def index():
    return render_template('index.html')
