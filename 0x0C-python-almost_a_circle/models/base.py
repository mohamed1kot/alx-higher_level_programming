#!/usr/bin/pyhton3
"""class Base"""


class Base:
    """
    Base class assign new value equal id if the id not None
    else increment __nb_objects and assign the new value
    to the public instance attribute id
    attribute:
        __nb_objects : private class attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor initiate the new class
        Args:
            id : public instance attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
