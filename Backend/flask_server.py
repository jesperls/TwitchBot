from flask import Flask, redirect, url_for, request, Response, jsonify
from flask_cors import CORS
import db_helper as db
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/get_commands', methods=['GET'])
def get_commands():
    response = json.loads(db.get_commands_json())
    # turn string back into json
    print(response)
    return response

@app.route('/api/add_command', methods=['POST'])
def add_command():
    if request.method == 'POST':
        data = request.get_json()
        db.add_command(data['command'], data['response'])
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False}), 403

    
@app.route('/api/remove_command', methods=['POST'])
def remove_command():
    if request.method == 'POST':
        data = request.get_json()
        db.remove_command(data['command'])
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False}), 403

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)