from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/o_nama")
def o_nama():
    return render_template("o_nama.html")

@app.route("/usluge")
def usluge():
    return render_template("usluge.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


if __name__ == "__main__":
    app.run()