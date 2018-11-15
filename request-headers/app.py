from flask import *

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello"


@app.route("/content-type", methods=["POST"])
def content_type():
    # Content-Typeがapplication/jsonでないならerrorを返す
    if not request.headers.get("Content-Type") == 'application/json':
        # JSON形式でエラーを返す
        return make_response(jsonify(res="error"), 400)
    # リクエストから飛んできたContent-Typeを返す
    return request.headers["Content-Type"]


if __name__ == "__main__":
    app.run(debug=True)
