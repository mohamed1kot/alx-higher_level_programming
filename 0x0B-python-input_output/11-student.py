#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """
    a class Student that defines a student
    Attributes:
        first_name: the first name of user.
        last_name: the last name of user.
        age: input age of user.
    """
    def __init__(self, first_name, last_name, age):
        """
        create the new instance of student

        Args:
            first_name: input the first name of the user.
            last_name: input the last name of the user.
            age : input the age of user.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        Args:
            attrs:  is a list of strings, only attribute
            names contained in this list must be retrieved.
        Return:
             a dictionary representation of a Student.
        """
        if attrs:
            new = {}
            for item in attrs:
                try:
                    new[item] = self.__dict__[item]
                except Exception:
                    pass
            return (new)
        return (self.__dict__)

    def reload_from_json(self, json):
        """
        """
        self.__dict__.update(json)
