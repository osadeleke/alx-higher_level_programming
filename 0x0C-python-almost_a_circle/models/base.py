#!/usr/bin/python3
"""
Base for other classes in the project
"""
import json


class Base:
    """
    Base for other classes in the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Dictionary to strings
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save Json to file
        """
        name = cls.__name__ + ".json"
        old_list = []
        for val in list_objs:
            ins_dict = {}
            for key, value in vars(val).items():
                if key.startswith("_{}_".format(cls.__name__)):
                    key = key[len(cls.__name__) + 3:]
                ins_dict[key] = value
            old_list.append(ins_dict)
        json_string = cls.to_json_string(old_list)
        with open(name, 'w') as f:
            f.write(json_string)
