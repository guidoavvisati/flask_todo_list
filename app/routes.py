from flask import render_template
from app import app
from app.database import query_name


@app.route("/")
def homepage():
    return render_template("index.html", name=query_name())
