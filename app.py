from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html')
