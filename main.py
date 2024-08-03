from flask import Flask,request,url_for,redirect,render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
     ust=request.form["sli"]
     return redirect(url_for('user', usr=ust))
    else:

     return render_template('login.html') 

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)