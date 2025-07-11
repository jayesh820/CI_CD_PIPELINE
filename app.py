import Flask from flask
app=Flask(__name__)
@app.route("/info")
def jayesh():
	return "hey i am jayesh"
@app.route("/phone")
def phone():
	return "7357557976"
app.run(host="0.0.0.0")