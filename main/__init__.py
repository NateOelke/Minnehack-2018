import logging
import sys
sys.path.insert(0, "src")
from injury_model import *
from flask import Flask, url_for, render_template, request
from main.config import Config

app = Flask(__name__)

# Set up injury model
X, y = load_data("data/database.csv")
input_dimensions = X.shape[1]
output_dimensions = 1
model = InjuryModel(input_dimensions, output_dimensions)
model.train_model(X, y)

def make_app(config = None, testing = None):
    if not config:
        if not testing:
            testing = False
        config = Config(testing=testing)

    # Create a Flask app object.

    app.config.from_object(config)

    import main.views as views
    app.register_blueprint(views.base.blueprint)

    return app

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html', say=request.form['age'], to=request.form['weight'])

if __name__ == "__main__":
    config = Config()
    app = make_app(config)
    app.run(port=config.port)
