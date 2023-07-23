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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of dictionaries from JSON
        """
        cont_list = []
        if json_string is None:
            return cont_list
        else:
            cont_list = json.loads(json_string)
            return cont_list

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save Json to file
        """
        name = cls.__name__ + ".json"
        old_list = []
        if list_objs is None:
            with open(name, 'w') as f:
                empty_list = json.dumps(old_list)
                f.write(empty_list)
            return
        for val in list_objs:
            ins_dict = {}
            for key, value in val.__dict__.items():
                if key.startswith("_{}_".format(cls.__name__)):
                    key = key[len(cls.__name__) + 3:]
                ins_dict[key] = value
            old_list.append(ins_dict)
        json_string = cls.to_json_string(old_list)
        with open(name, 'w') as f:
            f.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance of all attributes already set in dict
        """
        dum_inst = cls(1, 1, 1, 1, None)
        dum_inst.update(**dictionary)
        return dum_inst

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        name = cls.__name__ + ".json"
        with open(name, 'r') as f:
            cont = f.read()
        cont_list = cls.from_json_string(cont)
        fin_list = []
        for element in cont_list:
            fin_list.append(cls.create(**element))
        return fin_list
