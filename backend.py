from flask import Flask, escape, request, render_template, url_for
import json
import asyncio

app = Flask(__name__)
config = {}

with open('config.json') as f:
    config = json.load(f)


@app.route("/", methods=["GET"])
@app.route('/dashboard/', methods=["GET"])
def render_dashboard():
    return render_template('dashboard.html', config=config)


@app.route("/", methods=["POST"])
@app.route("/dashboard/", methods=["POST"])
def update_config():
    config = request.form
    with open("config.json", "w") as f:
        json.dump(config, f)
    return render_template("dashboard.html", config=config)


