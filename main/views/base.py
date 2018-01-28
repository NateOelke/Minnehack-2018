from flask import Blueprint, render_template

blueprint = Blueprint("base", __name__)

@blueprint.route("/")
def index():
<<<<<<< HEAD
    render_template("index.html")
=======
    return render_template('index.html')
>>>>>>> 8cf2f599db6c0316466a3657ccfdde883b5523dc
