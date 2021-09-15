"""
Copyright 2021, BYU-Idaho.
Author(s): Matt Manley, Jacob Oliphant
Version: 1.0
Date: 27-01-2021
"""
from collections import defaultdict
from genie.cast.actor import Actor

class Actors:
    """A collection of actors. 
    
    The responsibility of Actors is to keep track of them. It provides methods 
    for adding, removing and finding them in a variety of ways.
    
    You might be wondering why we don't just use dictionaries or other 
    generic collections in place of this class. Encapsulating actors in this 
    way gives us precise control over how they are modified. For example, we 
    might decide to delay removals instead of executing them immediately.
    
    Another important benefit of encapsulating actors this way is that it 
    allows us to change the underlying data structure and algorithms at any 
    time without affecting the rest of the project. 

    Attributes:
        _current_actors: Set[cls: Type[Actor]]
        _removed_actors: Set[cls: Type[Actor]]
    """

    def __init__(self):
        """Initializes a new instance of Cast."""
        self._current_actors = set()
        self._removed_actors = set()
        
    def add_actor(self, actor):
        """Adds the given actor to the cast.

        Args:
            actors: Actor, The actor to add.
        """
        self._current_actors.add(actor)
    
    def apply_changes(self):
        """Permantely removes all of the dead actors."""
        self._current_actors -= self._removed_actors
        self._removed_actors.clear()

    def remove_actor(self, actor):
        """Marks the given actor for removal from the cast. Clients must call clean_actors to permanently remove actors from the cast. 

        Args:
            actor: Actor, The actor to remove.
        """
        self._removed_actors.add(actor)
        
    def with_traits(self, *types):
        """Finds those actors with the given types of traits.

        Returns:
            set: A set of actors.
        """
        return [a for a in self._current_actors if a.has_traits(*types)]