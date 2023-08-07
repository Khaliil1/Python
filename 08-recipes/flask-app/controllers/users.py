from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipes')
def recipes():
    if not 'user_id' in session:
        return redirect('/')
    
    logged_user = User.get_by_id({'id':session['user_id']})
    recipes = Recipe.get_all()
    return render_template("recipes.html", user = logged_user, recipes = recipes)

@app.route('/users/create', methods=['POST'])
def register():
    print(request.form)
    
    if User.validate(request.form):

        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form,
            'password':pw_hash
        }

        user_id = User.create(data) 
        session['user_id'] = user_id
        return redirect('/recipes')
    
    return redirect('/')

@app.route('/login', methods =['POST'])
def login():
    
    user = User.get_by_email({'email':request.form['email']})
    if not user:
        flash("Invalid Email / Password", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email / Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/recipes')



@app.route('/logout', methods =['POST'])
def logout():
    session.clear()
    return redirect('/')