#!/usr/bin/python3
"""
Create a folder views inside v1
"""


from api.v1.views.places_reviews import *
from api.v1.views.places import *
from api.v1.views.users import *
from api.v1.views.amenities import *
from api.v1.views.states import *
from api.v1.views.index import *
from flask import Blueprint

"""
Create a folder views inside v1
"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
