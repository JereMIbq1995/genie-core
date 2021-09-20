import unittest
import sys
  
# setting path
sys.path.append('..\\..')
sys.path.append('..')

from genie.cast.actors import Actors
from genie.cast.actor import Actor
from stub.traits import Blue, Red, CanShoot

class TestActors(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up 3 different actors for the tests. Use the 3
        different traits combinations to differentiate between them
        """
        cls._actor1 = Actor()
        cls._actor1.add_trait(Blue())
        cls._actor1.add_trait(CanShoot())

        cls._actor2 = Actor()
        cls._actor2.add_trait(Blue())
        cls._actor2.add_trait(Red())

        cls._actor3 = Actor()
        cls._actor3.add_trait(Blue())
        cls._actor3.add_trait(Red())
        cls._actor3.add_trait(CanShoot())

    def setUp(self):
        # Create a brand new "empty" cast
        self._actors = Actors()

        # Assert that the cast is in deed empty
        self.assertNotIn(self._actor1, self._actors._current_actors)
        self.assertNotIn(self._actor2, self._actors._current_actors)
        self.assertNotIn(self._actor3, self._actors._current_actors)
        self.assertEqual(len(self._actors._current_actors), 0)

    def tearDown(self):
        pass

    def test_added_actor_found_in_current_actors_set_and_vice_versa(self):
        """
        Ensures that:
        - the added actor is found in the _current_actors set
        after add_actor is called
        - actors NOT yet added are NOT found in the _current_actors set.

        """

        # Add the first actor to the cast, ensures that actor1 is found but
        # actor2 and actor3 are not found
        self._actors.add_actor(self._actor1)
        self.assertIn(self._actor1, self._actors._current_actors)
        self.assertNotIn(self._actor2, self._actors._current_actors)
        self.assertNotIn(self._actor3, self._actors._current_actors)

        # Add the second actor to the cast, ensures that actor1 and actor2
        # are found, but actor3 is not found
        self._actors.add_actor(self._actor2)
        self.assertIn(self._actor1, self._actors._current_actors)
        self.assertIn(self._actor2, self._actors._current_actors)
        self.assertNotIn(self._actor3, self._actors._current_actors)

        # Add the third actor to the cast, ensures that actor1 and actor2
        # are still there, and actor3 is also found.
        self._actors.add_actor(self._actor3)
        self.assertIn(self._actor1, self._actors._current_actors)
        self.assertIn(self._actor2, self._actors._current_actors)
        self.assertIn(self._actor3, self._actors._current_actors)

    def test_removed_actor_found_in_removed_actors_set_and_vice_versa(self):
        """
        Ensures that:
        - the removed actor is found in the _removed_actors set
        after add_actor is called
        - actors NOT yet removed are NOT found in the _removed_actors set.

        """

        # Add the 3 actors to the cast without using add_actor so the test is
        # not dependent on the previous test
        self._actors._current_actors.add(self._actor1)
        self._actors._current_actors.add(self._actor2)
        self._actors._current_actors.add(self._actor3)

        # Assert that they are found:
        self.assertIn(self._actor1, self._actors._current_actors)
        self.assertIn(self._actor2, self._actors._current_actors)
        self.assertIn(self._actor3, self._actors._current_actors)

        # Remove the first actor to the cast, ensures that actor1 is found but
        # actor2 and actor3 are not found
        self._actors.remove_actor(self._actor1)
        self.assertIn(self._actor1, self._actors._removed_actors)
        self.assertNotIn(self._actor2, self._actors._removed_actors)
        self.assertNotIn(self._actor3, self._actors._removed_actors)

        # Remove the second actor to the cast, ensures that actor1 and actor2
        # are found, but actor3 is not found
        self._actors.remove_actor(self._actor2)
        self.assertIn(self._actor1, self._actors._removed_actors)
        self.assertIn(self._actor2, self._actors._removed_actors)
        self.assertNotIn(self._actor3, self._actors._removed_actors)

        # Remove the third actor to the cast, ensures that actor1 and actor2
        # are still there, and actor3 is also found.
        self._actors.remove_actor(self._actor3)
        self.assertIn(self._actor1, self._actors._removed_actors)
        self.assertIn(self._actor2, self._actors._removed_actors)
        self.assertIn(self._actor3, self._actors._removed_actors)

    def test_apply_changes_remove_removed_actors_from_current_actors(self):
        """
        Ensure that apply_changes() removes actors that were in the _removed_actors
        set from the _current_actors set
        """
        # Add the 3 actors to the cast without using add_actor so the test is
        # not dependent on the previous test. Also, add actor2 and actor3 to
        # the _removed_actors set in preparation for their actual removal
        self._actors._current_actors.add(self._actor1)
        self._actors._current_actors.add(self._actor2)
        self._actors._current_actors.add(self._actor3)

        self._actors._removed_actors.add(self._actor2)
        self._actors._removed_actors.add(self._actor3)

        # Create a copy of _removed_actors for latter comparison
        # because this set will be cleared
        removed_actors = [actor for actor in self._actors._removed_actors]

        # Assert that they are found:
        self.assertIn(self._actor1, self._actors._current_actors)
        self.assertIn(self._actor2, self._actors._current_actors)
        self.assertIn(self._actor3, self._actors._current_actors)
        self.assertIn(self._actor2, self._actors._removed_actors)
        self.assertIn(self._actor3, self._actors._removed_actors)

        # Now run the tested function:
        self._actors.apply_changes()

        # Make sure all actors in removed_actors are not found in _current_actors
        for actor in removed_actors:
            self.assertNotIn(actor, self._actors._current_actors)

    def test_apply_changes_clears_removed_actors(self):
        """
        Ensure that apply_changes() removes actors that were in the _removed_actors
        set from the _current_actors set
        """
        # Add the 3 actors to the cast without using add_actor so the test is
        # not dependent on the previous test. Also, add actor2 and actor3 to
        # the _removed_actors set in preparation for their actual removal
        self._actors._current_actors.add(self._actor1)
        self._actors._current_actors.add(self._actor2)
        self._actors._current_actors.add(self._actor3)

        self._actors._removed_actors.add(self._actor2)
        self._actors._removed_actors.add(self._actor3)

        # Assert that they are found:
        self.assertIn(self._actor1, self._actors._current_actors)
        self.assertIn(self._actor2, self._actors._current_actors)
        self.assertIn(self._actor3, self._actors._current_actors)
        self.assertIn(self._actor2, self._actors._removed_actors)
        self.assertIn(self._actor3, self._actors._removed_actors)

        # Now run the tested function:
        self._actors.apply_changes()

        # Ensure that the _removed_actors is cleared right after 
        # apply_changes() is called
        self.assertEqual(len(self._actors._removed_actors), 0)

    def test_with_traits_return_correct_actors(self):
        """
        Ensures that with_traits() returns only actors with the traits,
        and that the result set does not include any actor without one
        of the traits set forth in the parameters
        """
        # Add the 3 actors to the cast without using add_actor so the test is
        # not dependent on the previous test
        self._actors._current_actors.add(self._actor1)
        self._actors._current_actors.add(self._actor2)
        self._actors._current_actors.add(self._actor3)

        # Assert that they are found:
        self.assertIn(self._actor1, self._actors._current_actors)
        self.assertIn(self._actor2, self._actors._current_actors)
        self.assertIn(self._actor3, self._actors._current_actors)

        # All 3 actors have the Blue() trait, the return set should
        # include all 3
        actors_blue = self._actors.with_traits(Blue)
        self.assertIn(self._actor1, actors_blue)
        self.assertIn(self._actor2, actors_blue)
        self.assertIn(self._actor3, actors_blue)

        # Only 2 and 3 should return, 1 should NOT return
        actors_red = self._actors.with_traits(Red)
        self.assertIn(self._actor2, actors_red)
        self.assertIn(self._actor3, actors_red)
        self.assertNotIn(self._actor1, actors_red)

        # Only 1 and 3 should return, 2 should NOT return
        actors_canshoot = self._actors.with_traits(CanShoot)
        self.assertIn(self._actor1, actors_canshoot)
        self.assertIn(self._actor3, actors_canshoot)
        self.assertNotIn(self._actor2, actors_canshoot)

        # Only 1 and 3 should return, 2 should NOT return (query with a list of traits)
        actors_canshoot = self._actors.with_traits(CanShoot, Blue)
        self.assertIn(self._actor1, actors_canshoot)
        self.assertIn(self._actor3, actors_canshoot)
        self.assertNotIn(self._actor2, actors_canshoot)

        # Only 2 and 3 should return, 1 should NOT return (query with a list of traits)
        actors_red = self._actors.with_traits(Red, Blue)
        self.assertIn(self._actor2, actors_red)
        self.assertIn(self._actor3, actors_red)
        self.assertNotIn(self._actor1, actors_red)
        

if __name__ == "__main__":
    unittest.main()