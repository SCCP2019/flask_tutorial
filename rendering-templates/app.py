from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

@app.route("/<uname>")
def f(uname):
    return "Hello, %s!" % uname

@app.route("/t/<uname>")
def g(uname):
    return render_template('t.html', uname=uname)

if __name__ == "__main__":
    app.run(debug=True)
