import unittest
import sys

# setting path
sys.path.append('..\\..')
sys.path.append('..')

from genie_core.script.action import Action
from genie_core.script.actions import Actions
from genie_core.script.input_action import InputAction
from genie_core.script.output_action import OutputAction
from genie_core.script.update_action import UpdateAction

PRIORITY_ONE = 1
PRIORITY_TWO = 2
PRIORITY_THREE = 3

class TestAction(unittest.TestCase):
    
    # The following 3 nested classes are for testing purposes
    class TestInputAction(InputAction):
        def execute(self):
            pass
    
    class TestOutputAction(OutputAction):
        def execute(self):
            pass
    
    class TestUpdateAction(UpdateAction):
        def execute(self):
            pass

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self._actions = Actions()
        self._action1 = self.TestInputAction(PRIORITY_ONE)
        self._action2 = self.TestUpdateAction(PRIORITY_TWO)
        self._action3 = self.TestOutputAction(PRIORITY_THREE)

        self._action4 = self.TestInputAction(PRIORITY_TWO)
        self._action5 = self.TestOutputAction(PRIORITY_ONE)

    def tearDown(self):
        pass

    def test_add_action_puts_correct_action_in_current_actions_set(self):
        """
        Ensures that:
        Before add_action() is called, the action is not in current_actions list
        After add_action() is called, the action is found inside current_actions list
        """
        # First, ensure that the script is empty
        self.assertEqual(len(self._actions._current_actions), 0)

        # Now call add_action and ensure that the to-be-added action
        # is found in current_actions
        self._actions.add_action(self._action1)
        self.assertIn(self._action1, self._actions._current_actions)

        self._actions.add_action(self._action2)
        self.assertIn(self._action2, self._actions._current_actions)
        
        self._actions.add_action(self._action3)
        self.assertIn(self._action3, self._actions._current_actions)
    
    def test_removed_action_found_in_removed_actions_set_and_vice_versa(self):
        """
        Ensures that:
        - the removed action is found in the _removed_actions set
        after add_action is called
        - actions NOT yet removed are NOT found in the _removed_actions set.
        """
        # Add the 3 actors to the cast without using add_actor so the test is
        # not dependent on the previous test
        self._actions._current_actions.add(self._action1)
        self._actions._current_actions.add(self._action2)
        self._actions._current_actions.add(self._action3)

        # Assert that they are found:
        self.assertIn(self._action1, self._actions._current_actions)
        self.assertIn(self._action2, self._actions._current_actions)
        self.assertIn(self._action3, self._actions._current_actions)

        # Remove the first actor to the cast, ensures that actor1 is found but
        # actor2 and actor3 are not found
        self._actions.remove_action(self._action1)
        self.assertIn(self._action1, self._actions._removed_actions)
        self.assertNotIn(self._action2, self._actions._removed_actions)
        self.assertNotIn(self._action3, self._actions._removed_actions)

        # Remove the second actor to the cast, ensures that actor1 and actor2
        # are found, but actor3 is not found
        self._actions.remove_action(self._action2)
        self.assertIn(self._action1, self._actions._removed_actions)
        self.assertIn(self._action2, self._actions._removed_actions)
        self.assertNotIn(self._action3, self._actions._removed_actions)

        # Remove the third actor to the cast, ensures that actor1 and actor2
        # are still there, and actor3 is also found.
        self._actions.remove_action(self._action3)
        self.assertIn(self._action1, self._actions._removed_actions)
        self.assertIn(self._action2, self._actions._removed_actions)
        self.assertIn(self._action3, self._actions._removed_actions)

    def test_apply_changes_removing_removed_set_from_current_actions_set(self):
        """
        Ensures that the none of the actions found in removed_actions are
        found in current_actions after apply_changes() is called
        """
        # First, give the script a list of actions and removed actions.
        # This doesn't use add_action() so to not depend on the previous test
        self._actions._current_actions.add(self._action1)
        self._actions._current_actions.add(self._action2)
        self._actions._current_actions.add(self._action3)

        self._actions._removed_actions.add(self._action2)
        self._actions._removed_actions.add(self._action3)

        # Make a copy of _removed_actions since this set will be cleared
        # by apply_changes
        removed_actions = [action for action in self._actions._removed_actions]

        # Ensure that they are found
        self.assertIn(self._action1, self._actions._current_actions)
        self.assertIn(self._action2, self._actions._current_actions)
        self.assertIn(self._action3, self._actions._current_actions)
        self.assertIn(self._action2, self._actions._removed_actions)
        self.assertIn(self._action3, self._actions._removed_actions)

        # Now, let's call apply changes
        self._actions.apply_changes()

        # Make sure that none of the members of removed_actions are found in current_actions
        for action in removed_actions:
            self.assertNotIn(action, self._actions._current_actions)
    
    def test_apply_changes_clears_removed_actions(self):
        """
        Ensures that apply_changes() clears the _removed_actions set in preparation
        for the next frame.
        """
        # First, give the script a list of actions and removed actions.
        # This doesn't use add_action() so to not depend on the previous test
        self._actions._current_actions.add(self._action1)
        self._actions._current_actions.add(self._action2)
        self._actions._current_actions.add(self._action3)

        self._actions._removed_actions.add(self._action2)
        self._actions._removed_actions.add(self._action3)

        # Ensure that they are found
        self.assertIn(self._action1, self._actions._current_actions)
        self.assertIn(self._action2, self._actions._current_actions)
        self.assertIn(self._action3, self._actions._current_actions)
        self.assertIn(self._action2, self._actions._removed_actions)
        self.assertIn(self._action3, self._actions._removed_actions)

        # Now, let's call apply changes
        self._actions.apply_changes()

        # Make sure that _removed_actions is cleared (length = 0)
        self.assertEqual(len(self._actions._removed_actions), 0)
    
    def test_get_actions_return_all_actions_with_specfied_type(self):
        """
        Ensures that get_actions return all the correct actions in the
        _current_actions set and doesn't miss anything
        """
        # Add the 3 actions to the script without using add_actor so the test is
        # not dependent on the previous tests
        self._actions._current_actions.add(self._action1)
        self._actions._current_actions.add(self._action2)
        self._actions._current_actions.add(self._action3)
        self._actions._current_actions.add(self._action4)
        self._actions._current_actions.add(self._action5)

        # Assert that they are found:
        self.assertIn(self._action1, self._actions._current_actions)
        self.assertIn(self._action2, self._actions._current_actions)
        self.assertIn(self._action3, self._actions._current_actions)
        self.assertIn(self._action4, self._actions._current_actions)
        self.assertIn(self._action5, self._actions._current_actions)

        # INPUT: Only 1 and 4 should return, everything else should NOT return
        actions_INPUT = self._actions.get_actions(InputAction)
        self.assertIn(self._action1, actions_INPUT)
        self.assertIn(self._action4, actions_INPUT)
        self.assertNotIn(self._action2, actions_INPUT)
        self.assertNotIn(self._action3, actions_INPUT)
        self.assertNotIn(self._action5, actions_INPUT)

        # OUTPUT: Only 3 and 5 should return, everything else should NOT return
        actions_OUTPUT = self._actions.get_actions(OutputAction)
        self.assertIn(self._action3, actions_OUTPUT)
        self.assertIn(self._action5, actions_OUTPUT)
        self.assertNotIn(self._action1, actions_OUTPUT)
        self.assertNotIn(self._action2, actions_OUTPUT)
        self.assertNotIn(self._action4, actions_OUTPUT)

        # UPDATE: Only 2 should return, everything else should NOT return
        actions_UPDATE = self._actions.get_actions(UpdateAction)
        self.assertIn(self._action2, actions_UPDATE)
        self.assertNotIn(self._action1, actions_UPDATE)
        self.assertNotIn(self._action3, actions_UPDATE)
        self.assertNotIn(self._action4, actions_UPDATE)
        self.assertNotIn(self._action5, actions_UPDATE)
    
    def test_get_actions_return_result_sorted_by_priority(self):
        """
        Ensures that get_actions return a sorted result
        """
        # Add the 5 actions to the script without using add_actor so the test is
        # not dependent on the previous tests
        self._actions._current_actions.add(self._action1)
        self._actions._current_actions.add(self._action2)
        self._actions._current_actions.add(self._action3)
        self._actions._current_actions.add(self._action4)
        self._actions._current_actions.add(self._action5)

        # Assert that they are found:
        self.assertIn(self._action1, self._actions._current_actions)
        self.assertIn(self._action2, self._actions._current_actions)
        self.assertIn(self._action3, self._actions._current_actions)
        self.assertIn(self._action4, self._actions._current_actions)
        self.assertIn(self._action5, self._actions._current_actions)

        # 1 should be before 4 since 1 is priority 1, and 4 is priority 2
        actions_INPUT = self._actions.get_actions(InputAction)
        self.assertEqual(self._action1, actions_INPUT[0]) # Priority 1
        self.assertEqual(self._action4, actions_INPUT[1]) # Priority 2
        
        # 5 should be before 3 since 5 is priority 1, and 3 is priority 3
        actions_OUTPUT = self._actions.get_actions(OutputAction)
        self.assertEqual(self._action5, actions_OUTPUT[0]) # Priority 1
        self.assertEqual(self._action3, actions_OUTPUT[1]) # Priority 3
        
if __name__ == "__main__":
    unittest.main()
