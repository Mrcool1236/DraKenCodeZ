from flask import Flask, render_template, redirect, request, make_response
import flask
app = Flask(__name__,template_folder="./templates")

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/articles/hosting-discord-bot-on-heroku/")
def heroku():
	return render_template("/heroku/heroku.html")
	
if __name__ == "__main__":
	app.run(debug=True)
