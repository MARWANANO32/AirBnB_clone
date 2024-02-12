#!/usr/bin/python3
""" My class module
"""
import unittest
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def setUp(self):
        """_summary_
        """
        pass

    def tearDown(self):
        """_summary_
        """
        pass

    def test_instantiation(self):
        """_summary_
        """
        model = User()
        self.assertIsInstance(model, User)
        model2 = User(**model.to_dict())
        self.assertIsInstance(model2, User)

    def test_copying(self):
        """_summary_
        """
        model = User()
        model2 = User(**model.to_dict())
        self.assertDictEqual(model2.to_dict(), model.to_dict())

    def test_str(self):
        """_summary_
        """
        model = User()
        model_str = str(model)
        self.assertIsInstance(model_str, str)
        self.assertEqual(model_str, "[{}] ({}) {}".format(
            model.__class__.__name__,
            model.id,
            model.__dict__))

    def test_to_dict(self):
        """_summary_
        """
        model = User()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertDictEqual(model_dict, {
            **model.__dict__,
            '__class__': model.__class__.__name__,
            'created_at': datetime.datetime.isoformat(model.created_at),
            'updated_at': datetime.datetime.isoformat(model.updated_at),
        })
        self.assertIsInstance(model_dict['id'], str)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIsInstance(model_dict['__class__'], str)
        self.assertEqual(model_dict['__class__'], model.__class__.__name__)

    def test_save(self):
        """_summary_
        """
        model = User()
        updated_at = model.updated_at
        model_str = str(model)
        model_dict = model.to_dict()
        model.save()
        self.assertNotEqual(model.updated_at, updated_at)
        self.assertNotEqual(str(model), model_str)
        self.assertNotEqual(model.to_dict(), model_dict)
        model.updated_at = updated_at
        self.assertEqual(str(model), model_str)
        self.assertEqual(model.to_dict(), model_dict)
