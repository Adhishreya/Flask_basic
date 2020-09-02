#activte the virtual environment prior to running flask
#venv\scripts\activate
from flask import Flask,redirect,url_for
#constructor takes the current module as the argument
app=Flask(__name__)
@app.route("/")
def defa():
	return "Home page"
@app.route('/hello/<name>')
#route function is required for binding
def hello(name):
	return "hello %s "%name
@app.route("/admin")
def admin():
	return redirect(url_for("defa"))
@app.route("/signin")
#to redirect ti the function that has params use the following

def sign():
	return redirect(url_for("hello",name="admin"))


if __name__=='__main__':
	app.debug=True
	app.run()
	app.run(debug=True)
#host default(127.0.0.1),port(5000 default) ,options()
#for restaring automatically in the development cycle
#debugger manages the changes and also handles


# to run python filename.py

