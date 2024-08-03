from flask import Blueprint,request,redirect,url_for
from flask import render_template;

routes = Blueprint(__name__ ,'routes')

@routes.route('/', methods=['GET', 'POST'])
def hello():
    if request.methods == 'GET':
     ust=request.form['ust']
     return redirect(url_for('user', uid=ust))
    else:

     return render_template('index.html') 

@routes.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"