#!/usr/bin/python3
"""This module creates a Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class for managing place objects"""

    city_id = ""
    description = ""
    user_id = ""
    name = ""
    number_rooms = 0
    number_bathrooms = 0
    amenity_ids = []
    price_by_night = 0
    max_guest = 0
    latitude = 0.0
    longitude = 0.0
