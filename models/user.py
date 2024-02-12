#!/usr/bin/python3
"""_summary_
"""
from models.base_model import BaseModel


class User(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
