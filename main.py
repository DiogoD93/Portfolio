from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os

#Create flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("Flask_App")
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug= True, port= 5000)