#!/usr/bin/python3
""" My class module
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.engine.serialization import Serialization


class FileStorage():
    """_summary_
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """_summary_
        """
        return dict(self.__objects)

    def destroy(self, key):
        """_summary_
        """
        del self.__objects[key]
        return True

    def new(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        self.__objects[self.__get_obj_key(obj)] = obj

    def save(self):
        """_summary_
        """
        self.__save_to_file(self.__objects)

    def reload(self):
        """_summary_
        """
        for obj in self.__load_from_file():
            self.__objects[self.__get_obj_key(obj)] = obj

    def __load_from_file(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        content = ""
        try:
            with open(self.__file_path, "r") as f:
                content = f.read()
        except FileNotFoundError:
            pass
        if content == "":
            return []
        dict = Serialization.from_json_string(content)
        objs = []
        for obj in dict.values():
            objs.append(self.__get_obj_instance_from_class_name(obj))
        return objs

    def __get_obj_instance_from_class_name(self, obj):
        """_summary_
        """
        if obj['__class__'] == 'User':
            return User(**obj)
        elif obj['__class__'] == 'State':
            return State(**obj)
        elif obj['__class__'] == 'Review':
            return Review(**obj)
        elif obj['__class__'] == 'Place':
            return Place(**obj)
        elif obj['__class__'] == 'City':
            return City(**obj)
        elif obj['__class__'] == 'Amenity':
            return Amenity(**obj)
        else:
            return BaseModel(**obj)

    def __save_to_file(self, objs):
        """_summary_ - from 0x0C project

        Args:
            objs (_type_): _description_
        """
        objs_dict = {}
        for key in objs:
            objs_dict[key] = objs[key].to_dict()
        content = Serialization.to_json_string(objs_dict)
        with open(self.__file_path, "w") as f:
            f.write(content)

    def __get_obj_key(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        return "{}.{}".format(
            obj.__class__.__name__,
            obj.id)
