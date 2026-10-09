from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/internships")
def internships():
    company = "Amazon"
    return render_template("internships.html", company=company)

