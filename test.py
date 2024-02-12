#!/usr/bin/python3
from models import storage
from models.user import User

user = User()
print(user.to_dict())
