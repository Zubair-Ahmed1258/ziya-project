from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("menu.html")

@app.route("/details")
def details():
    return render_template("aboutus1.html")

@app.route("/webpage")
def web():
    return render_template("webpage.html")

@app.route("/contact")
def contact():
    return render_template("contactus.html")


if __name__ == "__main__":
    app.run(debug=True)