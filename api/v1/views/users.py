#!/usr/bin/python3
"""
create a new view for User
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users():
    """Retrieves the list of all User objects"""
    users = storage.all(User).values()
    users_list = []
    for user in users:
        users_list.append(user.to_dict())
    return jsonify(users_list)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User object"""
    users = storage.all(User)
    id = f"User.{user_id}"
    if id not in users:
        abort(404)
    user = users[id]
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    users = storage.all(User)
    id = f"User.{user_id}"
    if id not in users:
        abort(404)
    i = users[id]
    storage.delete(i)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Creates a User object"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'email' not in data:
        abort(400, 'Missing email')
    if 'password' not in data:
        abort(400, 'Missing password')
    user = User(email=data['email'], password=data['password'])
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """Updates a User object"""
    users = storage.all(User)
    id = f"User.{user_id}"
    if id not in users:
        abort(404)
    data = request.get_json()
    i = users[id]
    j = i.to_dict()
    for d in data:
        if d not in ["id", "email", "created_at", "updated_at"]:
            setattr(i, d, data[d])
    storage.save()
    return jsonify(j), 200
