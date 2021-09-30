"""
Copyright 2021, BYU-Idaho.
Author(s): Matt Manley, Jacob Oliphant
Version: 1.0
Date: 27-01-2021
"""
from abc import ABC


class Trait(ABC):
    """A distinguishing quality.

    The responsibility of Trait is to define the common methods for an actor's 
    specific qualities or features. Even though this version of Trait doesn't 
    define any it is still useful as a marker interface. That is, the intent of 
    a subclass is made clearer by virtue of the inheritance relationship with 
    this one.. 
    
    The concept of a "trait" is a fundamental part of the Genie object model. 
    Making sure it's represented in code, even as just a marker interface, 
    helps make the whole project more understandable. It also provides a place 
    to make changes in the future if we ever need it. 
    """
    pass    