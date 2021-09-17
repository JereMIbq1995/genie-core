import unittest
import sys
  
# setting path
sys.path.append('..\\..')
sys.path.append('..')

from genie.cast.actor import Actor
from stub.traits import Blue, Red, CanShoot

class TestActor(unittest.TestCase):

    def setUp(self):
        """
        This happens at the beginning of every test function.
        """
        self._actor = Actor()
    
    def tearDown(self) -> None:
        pass

    def test_add_trait(self):
        """
        Ensures that the trait given to the add trait function is
        in deed added to the actor._traits dictionary member variable
        """
        trait1 = Blue()
        self._actor.add_trait(trait1)
        self.assertIn(type(trait1), self._actor._traits.keys())
        self.assertIn(trait1, self._actor._traits.values())

        trait2 = Red()
        self._actor.add_trait(trait2)
        self.assertIn(type(trait2), self._actor._traits.keys())
        self.assertIn(trait2, self._actor._traits.values())

        trait3 = CanShoot()
        self._actor.add_trait(trait3)
        self.assertIn(type(trait3), self._actor._traits.keys())
        self.assertIn(trait3, self._actor._traits.values())
    
    def test_get_trait(self):
        """
        Ensures that:
        - if the trait doesn't exist, then get_trait() returns None
        - if a trait is in the _traits list of the actor, get_trait() returns that trait given the type
        """
        # Initially, neither Blue, Red, nor CanShoot is found in _actor._traits dictionary
        trait1 = Blue()
        self.assertIsNone(self._actor.get_trait(type(trait1)))
        trait2 = Red()
        self.assertIsNone(self._actor.get_trait(type(trait2)))
        trait3 = CanShoot()
        self.assertIsNone(self._actor.get_trait(type(trait3)))

        # Add each trait to the list and ensure that get_trait can pull it out correctly
        # Add the trait manually so that the test doesn't have to rely on the "add_trait" function, 
        #    which is tested in a different test.
        self._actor._traits[type(trait1)] = trait1
        self._actor._traits[type(trait2)] = trait2
        self._actor._traits[type(trait3)] = trait3
        self.assertEqual(self._actor.get_trait(type(trait1)), trait1)
        self.assertEqual(self._actor.get_trait(type(trait2)), trait2)
        self.assertEqual(self._actor.get_trait(type(trait3)), trait3)
    
    def test_has_traits(self):
        """
        First, give the actor a fix set of traits by storing it in _actor._traits
        Ensures that:
        - has_traits return true if a test set of traits is a subset of _actor._traits
        - has_traits return false if a test set of traits is NOT a subset of _actor._traits
        """
        
        # First, give the actor a fix set of 2 traits: (1)Blue and (3)CanShoot
        trait1 = Blue()
        trait2 = Red()
        trait3 = CanShoot()

        self._actor._traits[type(trait1)] = trait1
        self._actor._traits[type(trait3)] = trait3

        # For these cases, has_traits should return False:
        self.assertEqual(self._actor.has_traits(type(trait2)), False)
        self.assertEqual(self._actor.has_traits(type(trait2), type(trait1)), False)
        self.assertEqual(self._actor.has_traits(type(trait2), type(trait3)), False)

        # For these cases, has_traits should return True
        self.assertEqual(self._actor.has_traits(type(trait1)), True)
        self.assertEqual(self._actor.has_traits(type(trait3)), True)
        self.assertEqual(self._actor.has_traits(type(trait1), type(trait3)), True)

    def test_remove_traits(self):
        """
        First give the actor an initial set of traits
        Ensures that:
        - After remove_trait is called, the desired
        - 
        """


if __name__ == "__main__":
    unittest.main()