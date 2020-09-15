from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "1233222"

@app.route("/login")
def login():
    return "登录"

@app.route("/aoo")
def aoo():
    return "111"


if __name__ == '__main__':
    app.run()