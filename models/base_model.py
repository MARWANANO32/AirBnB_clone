#!/usr/bin/python3
""" My class module
"""
import uuid
import datetime
datetimeObj = datetime.datetime
now = datetimeObj.now


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

    def to_dict(self):
        """_summary_
        """
        return {
            **self.__dict__,
            '__class__': self.__class__.__name__,
            'created_at': datetimeObj.isoformat(self.created_at),
            'updated_at': datetimeObj.isoformat(self.updated_at),
        }
