import unittest
import sys
  
# setting path
sys.path.append('..\\..')
sys.path.append('..')

from genie.script.action import Action

class TestAction(unittest.TestCase):
    
    class MockAction(Action):
        def execute(self):
            print("executing")

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self._action1 = self.MockAction("PRIORITY_ONE")
        self._action2 = self.MockAction("PRIORITY_TWO")
        self._action3 = self.MockAction("PRIORITY_THREE")

    def tearDown(self):
        pass

    def test_get_priority_returns_correct_priority(self):
        """
        Ensures that get_priority returns the same priority
        passed to it originally
        """
        self.assertEqual(self._action1.get_priority(), "PRIORITY_ONE")
        self.assertEqual(self._action2.get_priority(), "PRIORITY_TWO")
        self.assertEqual(self._action3.get_priority(), "PRIORITY_THREE")
    
    def test_set_priority_correctly_changes_the_priority(self):
        """
        Ensures that the priority of the action whose "set_priority" function
        is called is changed to the appropriate priority
        """
        # Changing action1 to "PRIORITY_TWO":
        self._action1.set_priority("PRIORITY_TWO")
        self.assertEqual(self._action1._priority, "PRIORITY_TWO")

        # Changing action2 to "PRIORITY_THREE":
        self._action2.set_priority("PRIORITY_THREE")
        self.assertEqual(self._action2._priority, "PRIORITY_THREE")

        # Changing action3 to "PRIORITY_ONE":
        self._action3.set_priority("PRIORITY_ONE")
        self.assertEqual(self._action3._priority, "PRIORITY_ONE")

if __name__ == "__main__":
    unittest.main()