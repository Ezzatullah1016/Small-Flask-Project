from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1>Hello CLA</h1>"

@app.route("/")
def index():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
