#!/usr/bin/python3
""" My class module
"""
import uuid
import datetime
import models
datetimeObj = datetime.datetime
now = datetimeObj.now


class BaseModel():
    """ My class
    """

    def __init__(self, *args, **kwargs):
        """_summary_
        """
        if len(args) != 0:
            raise AttributeError("Args not handled for this object.")
        elif len(kwargs) != 0:
            self.id = kwargs['id']
            self.created_at = datetimeObj.fromisoformat(kwargs['created_at'])
            self.updated_at = datetimeObj.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = now()
            self.updated_at = now()
            models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """_summary_
        """
        return {
            **self.__dict__,
            '__class__': self.__class__.__name__,
            'created_at': datetimeObj.isoformat(self.created_at),
            'updated_at': datetimeObj.isoformat(self.updated_at),
        }
