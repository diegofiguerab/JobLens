from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to JobLens"

@app.route("/applications")
def applications():
    return "JobLens Applications"