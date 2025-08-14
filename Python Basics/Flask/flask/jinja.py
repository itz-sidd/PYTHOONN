##Building url dynamically
##Variable rule
##Jinja 2 Templaye engine

from flask import Flask,render_template,request,redirect,url_for


##Creating an instance of flask which is wsgi application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Hey this is my python web app<H1><html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

# @app.route("/form",methods=['GET','POST'])
# def form():
#     if request.method=='POST':
#         name=request.form['Name']
#         return f"Hello {name}"
#     return render_template('form.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['Name']
        return f"Hello {name}"
    return render_template('form.html')

#Variable rule
@app.route('/success/<int:score>')
def success(score):
    res=" "
    if score>50:
        res="PASSED"
    else:
        res="FAILED"

    return render_template('result.html',results=res)
    # return 'The marks you got is ' + str(score)

@app.route('/successers/<int:score>')
def successers(score):
    res=" "
    if score>50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score,'res':res}

    return render_template('result1.html',results=exp)

@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):

    return render_template('result.html',results=score)

app.route('/getresult')
def get_result():
    total_score=0
    return redirect(url_for('successers',score=total_score))


#Entry point of flask web app
if __name__=="__main__":
    app.run(debug=True)#By using debug we dont hve to restart server again n again