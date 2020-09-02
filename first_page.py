from flask import Flask,url_for,redirect,render_template
app=Flask(__name__)



@app.route("/")
def home():
	return render_template("index.html",content="Death",items=["Galaxy note 20","Galaxy Fold Z","iphone 8"])

if __name__=="__main__":
	app.debug=True
	app.run()
	app.run(debug=True)
