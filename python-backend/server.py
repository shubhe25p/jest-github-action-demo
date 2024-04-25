from flask import Flask, request
import json
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/add', methods=['POST'])
def addTodo():
    data = request.get_json()
    return 'Added a new todo!'

# @app.route('/getall')
# def getTodo():
#     alltodo = Todo.query.all()
#     return json.dumps([todo.as_dict() for todo in alltodo])


if __name__ == '__main__':
    app.run()
