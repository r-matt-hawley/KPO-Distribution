from pathlib import Path

from kpo_dist_api import config
from flask import render_template

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000)
