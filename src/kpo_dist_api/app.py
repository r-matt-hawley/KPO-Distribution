from pathlib import Path

from flask import render_template

from kpo_dist_api import config
# from kpo_dist_api.concerts import ConcertsResource

app = config.app

# config.api.add_resource(ConcertsResource)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    # app.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000)
    app.run(host="0.0.0.0", port=8000, debug=True)
