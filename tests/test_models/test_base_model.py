#!/usr/bin/python3
""" My class module
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
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
        self.assertIsInstance(BaseModel(), BaseModel)
