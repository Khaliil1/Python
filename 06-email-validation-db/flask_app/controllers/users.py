from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user import User


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", users=User.get_all())


@app.route("/submit", methods=["POST"])
def submit():
    print(request.form)
    if not User.is_valid(request.form):
        return redirect("/")
    User.save(request.form)
    return redirect("/")


@app.route("/users/destroy", methods=["POST"])
def destroy(id):
    data_dict = {"id": id}
    User.destroy(data_dict)
    return redirect("dashboard")
