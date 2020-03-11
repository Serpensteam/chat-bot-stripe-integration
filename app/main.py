from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from ...pagos Flask"

@app.route("/api/echo", methods=['POST'])
def create_share_link():
    return request.args
    


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)