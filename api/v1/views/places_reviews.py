#!/usr/bin/python3
"""
create a new view for Review
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/places/<place_id>/reviews',
                  methods=['GET'], strict_slashes=False)
def place_reviews(place_id):
    """Retrieves the list of all Review objects of a Place"""
    place = storage.all(Place)
    id = f"Place.{place_id}"
    if id not in place:
        abort(404)
    reviews = place.reviews
    reviews_list = []
    for review in reviews:
        reviews_list.append(review.to_dict())
    return jsonify(reviews_list)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """Retrieves a Review object"""
    review = storage.all(Review)
    id = f"Review.{review_id}"
    if id not in review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>',
                  methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """Deletes a Review object"""
    review = storage.all(Review)
    id = f"Review.{review_id}"
    if id not in review:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200

@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def post_review(place_id):
    """Creates a Review object"""
    place = storage.all(Place)
    id = f"Place.{place_id}"
    if id not in place:
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
    if 'text' not in data:
        abort(400, 'Missing text')
    review = Review(text=data['text'], place_id=place_id, user_id=user.id)
    storage.new(review)
    storage.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """Updates a Review object"""
    review = storage.all(Review)
    id = f"Review.{review_id}"
    if id not in review:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    ignore_keys = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
