#!/usr/bin/python3
"""This script is the base model."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class from which all other classes will inherit."""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes.

        Args:
            args: Unused arguments.
            kwargs: Dictionary of key-value arguments.
        """

        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "id":
                    self.id = kwargs["id"]
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns the official string representation of the instance."""

        return f"[<{type(self).__name__}>] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
