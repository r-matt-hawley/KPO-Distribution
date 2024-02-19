from pathlib import Path

from connexion import FlaskApp
from flask import render_template

app = FlaskApp(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000)
