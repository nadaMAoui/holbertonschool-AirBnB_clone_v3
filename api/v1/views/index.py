#!/usr/bin/python3
"""
import app_views from api.v1.views
create a route /status on the object
app_views that returns a JSON: "status" ok
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from models import amenity, city, place, review, state, user


@app_views.route('/status', strict_slashes=False)
def api_status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count():
    """Returns the number of each object by type"""
    counts = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(counts)
