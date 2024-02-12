#!/usr/bin/python3
"""_summary_
"""
from models.base_model import BaseModel


class User(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
