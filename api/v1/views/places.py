#!/usr/bin/python3
"""
create a new view for Place
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route('/cities/<city_id>/places',
                  methods=['GET'], strict_slashes=False)
def places(city_id):
    """Retrieves the list of all Place objects of a City"""
    city = storage.all(City)
    id = f"City.{city_id}"
    if id  not in city:
        abort(404)
    places = storage.all(Place).values()
    places_list = [p.to_dict() for p in places if p.city_id == city_id]
    return jsonify(places_list)


@app_views.route('/places/<place_id>',
                  methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """Retrieves a Place object"""
    place = storage.all(Place)
    id = f"Place.{place_id}"
    if id not in place:
        abort(404)
    p = place[id]
    return jsonify(p.to_dict())

@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object"""
    places = storage.all(Place)
    id = f"Place.{place_id}"
    if id not in places:
        abort(404)
    a = places[id]
    storage.delete(a)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places',
                  methods=['POST'], strict_slashes=False)
def post_place(city_id):
    """Creates a Place object"""
    city = storage.all(City)
    id = f"City.{city_id}"
    if id not in city:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    user = storage.all(User)
    id = f"User.{data['user_id']}"
    if id not in user:
        abort(404)
    if 'name' not in data:
        abort(400, 'Missing name')
    place = Place(name=data['name'],
                   user_id=data['user_id'], city_id=city_id)
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    storage.new(place)
    storage.save()
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>',
                  methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    """Updates a Place object"""
    place = storage.all(Place)
    id = f"Place.{place_id}"
    if id not in place:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict()), 200
