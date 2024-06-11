
import os
from flask import Flask, render_template
# from user import user

app = Flask(__name__)

def get_health_check():
    return {
        "status": "ok"
    }

@app.route("/")
def index():
    return "Index page"

@app.route("/template_test/<name>")
def template_test(name):
    return render_template('hello.html', person=name)

@app.route("/health_check")
def health_check():
    return get_health_check()
    
# @app.route("/user", methods=["GET"])
# def get_user():
#     return user


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)