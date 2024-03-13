# app.py

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return 'Hello from Flask!'

# Source: https://charisol.io/how-to-build-a-full-stack-web-application-with-python-and-vue-js/

from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = []
@app.route('/api/tasks', methods=['GET'])

def get_tasks():
    return jsonify(tasks)
@app.route('/api/tasks', methods=['POST'])

def add_task():
    data = request.get_json()
    task = data.get('task', '')
    tasks.append(task)
    return jsonify({'message': 'Task added successfully!'})

@app.route('/api/tasks/<int:index>', methods=['DELETE'])
def remove_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        return jsonify({'message': 'Task removed successfully!'})
    else:
        return jsonify({'error': 'Invalid index!'}), 400
