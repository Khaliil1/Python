from flask import render_template, redirect, request
from flask_app import app
from models.user_model import User


@app.route("/")
def dashboard():
    all_users = User.get_all()
    print(all_users)
    return render_template("dashboard.html", users=all_users)


@app.route("/users/new")
def signup():
    return render_template("signup.html")


@app.route("/users/create", methods=["POST"])
def create_users():
    data_dict = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.create_user(data_dict)
    return redirect("/")


@app.route("/users/<int:user_id>")
def show_user(user_id):
    data_dict = {"id": user_id}
    user = User.get_one_by_id(data_dict)
    return render_template("user_info.html", user=user)


# ---------------EDIT---------------------------------
@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    user_to_update = User.get_one_by_id({"id": user_id})
    return render_template("edit_user.html", user=user_to_update)


@app.route("/users/<int:user.id>/update", methods=["POST"])
def update_user(user_id):
    data_dict = {**request.form}
    data_dict["id"] = user_id
    User.update(data_dict)
    return redirect(f"/users/{user_id}")


# ---------------DELETE-------------------------------


@app.route("/users/<int:user_id>/destroy", methods=["POST"])
def delete(user_id):
    data_dict = {"id": user_id}
    User.delete(data_dict)
    return redirect("/")
