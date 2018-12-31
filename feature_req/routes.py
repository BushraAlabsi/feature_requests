
from feature_req import app


@app.route("/")
def hello():
    return "hello"