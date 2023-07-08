#!/usr/bin/python3
"""
create a new view for City
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def cities(state_id):
    list = []
    states = storage.all(State)
    id = f"State.{state_id}"
    if id not in states:
        abort(404)
    city = storage.all(City).values()
    for s in city:
        ci = s.to_dict()
        if "state_id" in ci:
            if ci["state_id"] == state_id:
                list.append(s.to_dict())
    return jsonify(list)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves a city object"""
    city = storage.all(City)
    id = f"City.{city_id}"
    if id not in city:
        abort(404)
    sity = city[id]
    return jsonify(sity.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    city = storage.all(City)
    id = f"City.{city_id}"
    if id not in city:
        abort(404)
    de = city[id]
    storage.delete(de)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def post_city(state_id):
    states = storage.all(State)
    id = f"State.{state_id}"
    if id not in states:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    city = City(name=data['name'], state_id=state_id)
    storage.new(city)
    storage.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def put_city(city_id):
    city = storage.all(City)
    id = f"City.{city_id}"
    if id not in city:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    i = city[id]
    j = i.__dict__
    for d in data:
        if d not in ["id", "created_at",
                     "updated_at"]:
            j[d] = data[d]
    storage.save()
    return jsonify(j), 200
