from flask import Flask,render_template


##Creating an instance of flask which is wsgi application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Hey this is my python web app<H1><html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

#Entry point of flask web app
if __name__=="__main__":
    app.run(debug=True)#By using debug we dont hve to restart server again n again