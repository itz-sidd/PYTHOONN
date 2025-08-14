from flask import Flask


##Creating an instance of flask which is wsgi application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the python continuation,it is rushing n thrilling"

@app.route("/index")
def index():
    return "this is the index page"

#Entry point of flask web app
if __name__=="__main__":
    app.run(debug=True)#By using debug we dont hve to restart server again n again