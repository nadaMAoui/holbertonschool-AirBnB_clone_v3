#!/usr/bin/python3
"""
This script creates a Flask application instance and configures it.

It sets up the necessary components for the API, including routes, error handlers, and database connections.
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.register_blueprint(app_views)


@app.route("/")
def hello():
    """
    This route returns a simple "hello" message.

    It is a test route to verify that the application is running correctly.
    """
    return "hello"


@app.teardown_appcontext
def teardown_db(exception):
    """
    This function is called when the application context is torn down.

    It ensures that the database connection is properly closed to prevent resource leaks.
    """
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """
    This error handler is triggered when a 404 error occurs.

    It returns a JSON response with an error message indicating that the requested resource was not found.
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)

