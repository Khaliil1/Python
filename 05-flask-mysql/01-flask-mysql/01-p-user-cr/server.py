from flask import Flask, render_template, redirect, request
from user_model import User

app = Flask(__name__)


@app.route('/')
def dashboard():
    all_users = User.get_all()
    print(all_users)
    return render_template('dashboard.html', users= all_users)

@app.route('/users/new')
def signup():
    return render_template("signup.html")

@app.route('/users/create', methods = ['POST'])
def create_users():
    print(request.form)
    data_dict = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        
    }
    User.create_user(data_dict)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)