"""
Defines the person class that wil be the base class for students and instructors
"""


class Person:
    """
    the perso class is the base class for defining all people in the plums enviornment, including students and instructors, and captures all of the basic properties common to both of thes subclasses
    """


    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
