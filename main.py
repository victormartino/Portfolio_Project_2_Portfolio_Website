from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/unavailable')
def unavailable():
    return render_template("unavailable.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)
