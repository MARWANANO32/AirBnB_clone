#!/usr/bin/python3
""" My class module
"""
import uuid
import datetime
now = datetime.datetime.now


class BaseModel():
    """ My class
    """

    def __init__(self):
        """_summary_
        """
        self.id = str(uuid.uuid4())
        self.created_at = now()
        self.updated_at = now()

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """_summary_
        """
        self.updated_at = now()
