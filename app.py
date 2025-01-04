from flask import Flask

app = Flask(__name__)

@app.route("/info")
def dipak():
    return "hello From Dipak"

app.run(host="0.0.0.0")
