"""
Copyright 2021, BYU-Idaho.
Author(s): Matt Manley, Jacob Oliphant
Version: 1.0
Date: 27-01-2021
"""


class Actor:
    """A thing that participates in an animation. 
    
    The responsibility of Actor is to keep track of its traits. The concept of 
    an "actor" is very broad indeed. It could be a character, the background, 
    scoreboard or even something unseen like a sensor or monitor. 
    
    The combination of actors and traits are an important part of the Genie 
    object model. Together they provide great flexibility in defining the 
    attributes and behaviors of the participants in your project without 
    having to resort to deep inheritance hierarchies. You can mix and match 
    them to create any kind of actor you want.

    Attributes:
        _traits: Dict[Type[Trait], cls: Type[Trait]], The actor's traits.
    """

    def __init__(self):
        """Initializes a new instance of Actor."""
        self._traits = dict()
            
    def add_trait(self, trait):
        """Adds the given trait to the actor. Will replace 

        Args:
            trait: Trait, The trait to add.
        """
        type_ = type(trait)
        self._traits[type_] = trait
        
    def get_trait(self, type_):
        """Gets the trait corresponding to the given type. This method will 
        return None if the type of trait could not be found.

        Args:
            type_: Type[Trait], The type of trait to get.
        
        Returns:
            cls: Type[Trait], The corresponding trait or None.
        """
        return self._traits.get(type_, None)
        
    def has_traits(self, *types):
        """Whether or not the actor has all of the given types of trait.

        Args:
            types: Tuple[Type[Trait]], The trait types.

        Returns:
            boolean: True if the actor has all the traits; false if otherwise.
        """
        return set(types).issubset(self._traits.keys())

    def remove_trait(self, trait):
        """Removes the given trait from the actor.

        Args:
            trait: Trait, The trait to remove.
        """
        type_ = type(trait)
        self._traits.pop(type_, None)