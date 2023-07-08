#!/usr/bin/python3
"""
create a new view for Amenity
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def amenities():
    """Retrieves the list of all Amenity objects"""
    amenities = storage.all(Amenity).values()
    amenities_list = []
    for amenity in amenities:
        amenities_list.append(amenity.to_dict())
    return jsonify(amenities_list)


@app_views.route('/amenities/<amenity_id>',
                  methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves a Amenity object"""
    amenities = storage.all(Amenity)
    id = f"Amenity.{amenity_id}"
    if id not  in amenities:
        abort(404)
    amenity = amenities[id]
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>',
                  methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """Deletes a Amenity object"""
    amenities = storage.all(Amenity)
    id = f"Amenity.{amenity_id}"
    if id  not  in amenities:
        abort(404)
    i = amenities[id]
    storage.delete(i)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
    """Creates a Amenity object"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    amenity = Amenity(name=data['name'])
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>',
                  methods=['PUT'], strict_slashes=False)
def put_amenity(amenity_id):
    """Updates a Amenity object"""
    amenities = storage.all(Amenity)
    id = f"Amenity.{amenity_id}"
    if id not in amenities:
        abort(404)
    data = request.get_json()
    i = amenities[id]
    j = i.__dict__
    for d in data:
        if i not in ["id", "created_at",
                     "updated_at"]:
            i[d] = data[d]
    storage.save()
    return jsonify(j.to_dict()), 200
