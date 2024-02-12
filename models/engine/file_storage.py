#!/usr/bin/python3
""" My class module
"""
from models.base_model import BaseModel
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
        return [BaseModel(**obj) for obj in dict.values()]



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
