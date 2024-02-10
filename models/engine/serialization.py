#!/usr/bin/python3
""" My class module
"""
import json


class Serialization():
    """_summary_
    """
    
    @staticmethod
    def from_json_string(json_string):
        """_summary_

        Args:
            json_string (_type_): _description_
        """
        is_none = json_string is None
        not_str = type(json_string) is not str
        if is_none or not_str or json_string == '':
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(objs):
        """_summary_ - from 0x0C project

        Args:
            objs (_type_): _description_
        """
        is_none = objs is None
        not_dict = type(objs) is not dict
        if is_none or not_dict or len(objs) == 0:
            return "\{\}"
        return json.dumps(objs)
