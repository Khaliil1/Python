from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "counters"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:    
        session["count"] += 1
    
    return render_template("counter.html")    

@app.route("/count", methods=["POST"])
def view_count():
    if request.form["alter"]=="add":
        session["count"] += 1
    elif request.form["alter"]=="reset":
        session["count"] = 0

    return redirect("/")

@app.route("/delete")
def delete():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    
    app.run(debug=True, port="5000") 