# You don't import the flask framework
# you import the Flask class from the flask framework

from flask import Flask

# once Flask class is imported, 
# you are instantiating the object
# __name__ is a variable that gets as a value the name of the script

app = Flask(__name__)
@app.route('/')
def home():
    var = 'Go to hell world'
    var += '<br/><a href="localhost:5000/about">Go to About</a> now'
    return var

@app.route('/about')    
def about():
    return 'this is the about page but still go to hell'
    return '<a href="localhost:5000/" >Go home</a>'

# when you execute the script, the __name__ variable
# will take on the value '__main__'
if __name__ == '__main__':
    app.run(debug = True)
    
# on the other hand, if you import a script, 
# the __name__ variable will be named after the name of the script/file