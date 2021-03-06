# from flask import Flask, render_template, request
from flask import *

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    # NOTE: None は値が存在しないことを示す定数
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"], request.form["password"]):
            return log_the_user_in(request.form["username"])
        else:
            error = "Invalid username/password"
    return render_template("login.html", error=error)


def valid_login(username=None, password=None):
    # NOTE: まだデータベースなどのシステムを使えないためにユーザー認証の実装ができないのでハードコードした値と比較しています.
    if username == "student" and password == "password" : # 好きな値に変更してみてください
        return True
    return False


def log_the_user_in(name=None):
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
