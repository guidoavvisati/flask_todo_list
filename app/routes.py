from flask import render_template
from app import app
import app.database as db


@app.route("/")
def homepage():
    return render_template("index.html", items=db.fetch_todo())
