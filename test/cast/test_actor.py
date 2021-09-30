import unittest
import sys
  
# setting path
sys.path.append('..\\..')
sys.path.append('..')

from genie_core.cast.actor import Actor
from stub.traits import Blue, Red, CanShoot

class TestActor(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """
        Initialize the traits to be used in each test.
        """
        print("setUpClass")
        cls._trait1 = Blue()
        cls._trait2 = Red()
        cls._trait3 = CanShoot()

    def setUp(self):
        """
        This happens at the beginning of every test function.
        """
        # Before any test, make sure the actor of interest is new
        # and doesn't have any trait
        self._actor = Actor()
    
    def tearDown(self) -> None:
        """
        This happens at the end of every test function.
        """
        pass

    def test_add_trait(self):
        """
        Ensures that the trait given to the add trait function is
        in deed added to the actor._traits dictionary member variable
        """
        print(type(self._trait1))
        print(type(self._trait2))
        print(type(self._trait3))
        
        # Add trait1, ensures that the key can be found, value can be found,
        # and that the key for trait1 actually maps to trait1
        self._actor.add_trait(self._trait1)
        self.assertIn(type(self._trait1), self._actor._traits.keys())
        self.assertIn(self._trait1, self._actor._traits.values())
        self.assertEqual(self._actor._traits[type(self._trait1)], self._trait1)

        # Add trait2, ensures the same thing as with trait1
        self._actor.add_trait(self._trait2)
        self.assertIn(type(self._trait2), self._actor._traits.keys())
        self.assertIn(self._trait2, self._actor._traits.values())
        self.assertEqual(self._actor._traits[type(self._trait2)], self._trait2)

        # Add trait3
        self._actor.add_trait(self._trait3)
        self.assertIn(type(self._trait3), self._actor._traits.keys())
        self.assertIn(self._trait3, self._actor._traits.values())
        self.assertEqual(self._actor._traits[type(self._trait3)], self._trait3)
    
    def test_get_trait_returns_none_when_actor_doesnot_have_trait(self):
        """
        Ensures that:
        - if the trait doesn't exist, then get_trait() returns None
        """
        # Initially, neither Blue, Red, nor CanShoot is found in _actor._traits dictionary
        self.assertIsNone(self._actor.get_trait(type(self._trait1)))
        self.assertIsNone(self._actor.get_trait(type(self._trait2)))
        self.assertIsNone(self._actor.get_trait(type(self._trait3)))

    def test_get_trait_returns_correct_trait_when_actor_has_trait(self):
        """
        Ensures that
        - if a trait is in the _traits list of the actor, get_trait() returns that trait given the type
        """
        # Add each trait to the list and ensure that get_trait can pull it out correctly
        # Add the trait manually so that the test doesn't have to rely on the "add_trait" function, 
        #    which is tested in a different test.
        
        self._actor._traits[type(self._trait1)] = self._trait1
        self._actor._traits[type(self._trait2)] = self._trait2
        self._actor._traits[type(self._trait3)] = self._trait3
        self.assertEqual(self._actor.get_trait(type(self._trait1)), self._trait1)
        self.assertEqual(self._actor.get_trait(type(self._trait2)), self._trait2)
        self.assertEqual(self._actor.get_trait(type(self._trait3)), self._trait3)
    
    def test_has_traits_returning_true(self):
        """
        First, give the actor a fix set of traits by storing it in _actor._traits
        Ensures that:
        - has_traits return true if a test set of traits is a subset of _actor._traits
        """
        
        # First, give the actor an initial set of 2 traits: (1)Blue and (3)CanShoot
        
        self._actor._traits[type(self._trait1)] = self._trait1
        self._actor._traits[type(self._trait3)] = self._trait3

        # For these cases, has_traits should return True
        self.assertEqual(self._actor.has_traits(type(self._trait1)), True)
        self.assertEqual(self._actor.has_traits(type(self._trait3)), True)
        self.assertEqual(self._actor.has_traits(type(self._trait1), type(self._trait3)), True)
    
    def test_has_traits_returning_false(self):
        """
        Ensures that:
        - has_traits return false if a test set of traits is NOT a subset of _actor._traits
        """
        # First, give the actor a fix set of 2 traits: (1)Blue and (3)CanShoot
        self._actor._traits[type(self._trait1)] = self._trait1
        self._actor._traits[type(self._trait3)] = self._trait3

        # For these cases, has_traits should return False:
        self.assertEqual(self._actor.has_traits(type(self._trait2)), False)
        self.assertEqual(self._actor.has_traits(type(self._trait2), type(self._trait1)), False)
        self.assertEqual(self._actor.has_traits(type(self._trait2), type(self._trait3)), False)

    def test_removed_trait_not_in_traits_dictionary(self):
        """
        First give the actor an initial set of traits
        Ensures that:
        - After remove_trait is called, the removed trait is not found in the traits
        dictionary, and that the "new traits set = old traits set - removed trait".
        """
        
        # First, give the actor a fix set of traits
        self._actor._traits[type(self._trait1)] = self._trait1
        self._actor._traits[type(self._trait2)] = self._trait2

        # Remove trait1, ensure that afterwards, trait1 is not found in _traits
        self._actor.remove_trait(self._trait1)
        self.assertNotIn(type(self._trait1), self._actor._traits.keys())

        # Remove trait2, ensure that afterwards, trait2 is not found in _traits
        self._actor.remove_trait(self._trait2)
        self.assertNotIn(type(self._trait2), self._actor._traits.keys())

    def test_removed_trait_is_the_ONLY_thing_that_gets_removed(self):
        """
        First give the actor an initial set of traits
        Ensures that:
        - "new traits set = old traits set - removed trait".
        """
        # First, give the actor an initial set of traits
        self._actor._traits[type(self._trait1)] = self._trait1
        self._actor._traits[type(self._trait2)] = self._trait2

        # Remove trait1, ensure that afterwards, there's only trait2 left
        self._actor.remove_trait(self._trait1)
        self.assertDictEqual(self._actor._traits, { type(self._trait2): self._trait2 } )

        # Remove trait2, ensure that afterwards, the traits dictionary is empty
        self._actor.remove_trait(self._trait2)
        self.assertDictEqual(self._actor._traits, {} )
        
    def test_removed_trait_not_found_in_dictionary(self):
        """
        Ensures that:
        - If the to-be-removed trait is not found in the traits dictionary, 
        the _traits dictionary stays the same after the call
        """
        
        # First, give the actor an initial set of traits
        self._actor._traits[type(self._trait1)] = self._trait1
        self._actor._traits[type(self._trait2)] = self._trait2

        # Before attempting to call remove_trait, make a copy of the initial state
        # of the traits dictionary
        initialDict = {k: self._actor._traits[k] for k in self._actor._traits}

        # Attempt to remove a trait that's not in self._actor._traits
        self._actor.remove_trait(self._trait3)

        # Ensures that the new _traits dictionary after the remove_trait call is
        # the same as its initial state.
        self.assertDictEqual(initialDict, self._actor._traits)


if __name__ == "__main__":
    unittest.main()