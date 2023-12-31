#!/usr/bin/python3
"""
FileStorage module

Implements the FileStorage class responsible for serializing instances to a JSON file
and deserializing JSON file to instances.
"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}
    __classes = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

        self.__classes[obj.__class__.__name__] = obj.__class__

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        self.update_classes()
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        from models.base_model import BaseModel  # Move the import here

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_cls = globals().get(class_name)
                    if obj_cls:
                        self.__classes[class_name] = obj_cls
                        self.__objects[key] = obj_cls(**value)
        except FileNotFoundError:
            pass
