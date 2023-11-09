#!/usr/bin/python3
"""
FileStorage tests
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        # Create a BaseModel instance
        base_model = BaseModel()
        base_model_key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.storage.new(base_model)
        self.storage.save()

        # Check if all method returns the stored objects
        all_objects = self.storage.all()
        self.assertIn(base_model_key, all_objects)
        self.assertEqual(all_objects[base_model_key], base_model)

    def test_save_reload(self):
        # Create a BaseModel instance
        base_model = BaseModel()
        base_model_key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.storage.new(base_model)
        self.storage.save()

        # Reload the storage
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded storage has the stored object
        reloaded_objects = new_storage.all()
        self.assertIn(base_model_key, reloaded_objects)
        reloaded_base_model = reloaded_objects[base_model_key]

        # Check if the reloaded object is of the correct type and has the same attributes
        self.assertIsInstance(reloaded_base_model, BaseModel)
        self.assertEqual(reloaded_base_model.__dict__, base_model.__dict__)

if __name__ == '__main__':
    unittest.main()
