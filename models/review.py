#!/usr/bin/python3
""" the review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """review class """
    place_id = ""
    user_id = ""
    text = ""
