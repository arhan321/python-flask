#!/usr/bin/env python3

from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    if not data or not 'nama' in data or not 'umur' in data:
        return jsonify({"error": "Data tidak lengkap"}), 400
    
    user = {
        'id': len(users) + 1, 
        'nama': data['nama'],
        'umur': data['umur']
    }
    
    users.append(user)
    
    return jsonify({"message": "Data berhasil dibuat", "user": user}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def show_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User tidak ditemukan"}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        if 'nama' in data:
            user['nama'] = data['nama']
        if 'umur' in data:
            user['umur'] = data['umur']
        return jsonify({"message": "Data berhasil diperbarui", "user": user}), 200
    else:
        return jsonify({"error": "User tidak ditemukan"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({"message": "User berhasil dihapus"}), 200

if __name__ == '__main__':
    app.run(debug=True)
