from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.author import Author

@app.route('/')
def index():
    all_authors = Author.get_all()
    return render_template("index.html" ,authors= all_authors)


@app.route('/authors/create', methods=['POST'])
def create_author():
    Author.create(request.form)
    return redirect('/')
