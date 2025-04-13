from flask import Flask,render_template,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jalaba.html")
def jaloba():
    return render_template("jalaba.html")


if __name__ =="__main__":
    app.run(debug=True)
