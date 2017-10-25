#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message":"Hello, World!"})

@app.route('/post', methods=['POST'])
def post():
    received = request.get_json()
    print received
    return jsonify({'data' : received})

if __name__ == '__main__':
    app.run(debug=True)