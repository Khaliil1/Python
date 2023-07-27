from flask import render_template, redirect, request
from flask_app import app
from models.dojo_model import Dojo


@app.route("/")
def Dojo_info():
    all_Dojos = Dojo.get_all()
    print(all_Dojos)
    return render_template("Dojo_info.html", Dojos=all_Dojos)


@app.route("/Dojos/new")
def index():
    return render_template("index.html")


@app.route("/Dojos/create", methods=["POST"])
def create_Dojo():
    if Dojo.validate_dojo(request.form):
        data_dict = {
            "name": request.form["name"],
            "dojo_location": request.form["dojo_location"],
            "fav_language": request.form["fav_language"],
            "comment": request.form["comment"],
        }
    Dojo.create_Dojo(data_dict)
    return redirect("/")


# @app.route("/dojo_s", methods=["POST"])
# def dojo_s():
#     if Dojo.validate_dojo(request.form):
#         return redirect("/")
#     return redirect("/dojo_info.html")


@app.route("/Dojos/<int:Dojo_id>")
def show_Dojo(Dojo_id):
    data_dict = {"id": Dojo_id}
    Dojo = Dojo.get_one_by_id(data_dict)
    return render_template("Dojo_info.html", Dojo=Dojo)
