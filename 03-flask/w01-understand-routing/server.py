from flask import Flask  

app = Flask(__name__)    




@app.route('/')          
def hello_world():
    return 'Hello World!' 


    
@app.route('/dojo')
def success():
    return 'dojo!'     


@app.route('/say/<name>')
def say_hi(name):
    return f" hi {name}"

@app.route('/repeat/<time>/<name>')
def yaya(name,time):
    return f" {name}<br>"  * int(time)

if __name__=="__main__":  
    app.run(debug=True, port=5000)  

