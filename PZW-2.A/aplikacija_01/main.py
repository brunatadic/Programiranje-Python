from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/o_nama")
def o_nama():
    return "O nama"

if __name__=="__main__":
    app.run()