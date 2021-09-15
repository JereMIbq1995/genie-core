"""
Copyright 2021, BYU-Idaho.
Author(s): Matt Manley, Jacob Oliphant
Version: 1.0
Date: 27-01-2021
"""
from genie.script.input_action import InputAction
from genie.script.output_action import OutputAction
from genie.script.update_action import UpdateAction


class Actions:
    """A collection of actions.

    The responsibility of Actions is to keep track of them. It provides methods 
    for adding, removing and finding them in a variety of ways.
    
    Attributes:
        _actions: Dict[str, List[Action]]), The actions in the script.
    """

    def __init__(self):
        """Initializes a new instance of Script."""
        self._current_actions = set()
        self._removed_actions = set()
        
    def add_action(self, action):
        """Add the given action to the script.

        Args:
            action: Action, The action to add.
        """
        self._current_actions.add(action)
        
    def apply_changes(self):
        """Permantely removes all of the dead actors."""
        self._current_actions -= self._removed_actions
        self._removed_actions.clear()

    def remove_action(self, action):
        """Removes the given action from the script.
        
        Args:
            action (Action): The action to remove.
        """
        self._removed_actions.add(action)
 
    def get_actions(self, type_):
        """Gets the actions with the given type.
        
        Args:
            type_: str, The actions's type.
        
        Returns:
            List[Action]: A list of actions.
        """
        return sorted(a for a in self._current_actions if isinstance(a, type_),
            key=lambda x: x.get_priority())