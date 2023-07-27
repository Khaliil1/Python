from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user import User


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return redirect("/")


@app.route("/submit", methods=["POST"])
def submit():
    print(request.form)
    user_from_db = User.get_by_email({"email": request.form["email"]})
    if user_from_db:
        flash("Email is not valid !!!", "submit")
    return redirect("/")


@app.route("/users/<int:user_id>/destroy", methods=["POST"])
def delete(user_id):
    data_dict = {"id": user_id}
    User.delete(data_dict)
    return redirect("/")
