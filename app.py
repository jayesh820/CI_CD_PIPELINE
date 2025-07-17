from flask import Flask 
app=Flask(__name__)
@app.route("/info")
def jayesh():
	return "hey i am jayesh"
@app.route("/phone")
def phone():
	return "412942087976"
app.run(host="0.0.0.0")
