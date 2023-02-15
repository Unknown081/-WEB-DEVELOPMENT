# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():
    name = "Devu" 
    age = "14" 
    return render_template('index.html' , name = name , age = age)
# define the route to father webpage
@app.route("/father")
def home():
    name = "Father"
    age = "50"
    return render_template('father.html', name= name , age= age)
# define the route to mother webpage
@app.route("/Mother")
def home():
    name = "mother"
    age = "54"
    return render_template('mother.html', name= name , age= age)

# define the route to friends webpage
@app.route("/friend")
def home():
    name = "friend"
    age = "14"
    return render_template('friend.html', name= name , age= age)

if __name__  ==  '__main__':
    app.run(debug=True)
