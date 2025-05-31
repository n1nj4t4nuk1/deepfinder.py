import unittest

from deepfinder import deep_find


class TestFindInfrozenSets(unittest.TestCase):
    def test_first_value_of_a_frozen_set(self):
        """
        Test that deep_find can access the first value of a frozen set using numeric index.
        
        This test verifies that deep_find can access elements in a frozen set using
        numeric indices, similar to how lists are accessed. It tests the basic
        functionality of accessing the first element (index 0) of a frozen set.
        
        Expected: deep_find(frozenset((1, 2, 3)), '0') -> 1
        """
        data = frozenset((1, 2, 3))
        result = deep_find(data, '0')
        self.assertEqual(result, 1)

    def test_frozen_set_access_by_non_numeric_value(self):
        """
        Test that deep_find returns None when trying to access a frozen set with a non-numeric index.
        
        This test verifies that deep_find handles invalid access attempts gracefully
        when trying to access a frozen set using a non-numeric index. Since frozen
        sets can only be accessed by numeric indices, any other type of index
        should return None.
        
        Expected: deep_find(frozenset((1, 2, 3)), 'b') -> None
        """
        data = frozenset((1, 2, 3))
        result = deep_find(data, 'b')
        self.assertEqual(result, None)

    def test_frozen_set_access_by_not_hashable_json(self):
        """
        Test that deep_find returns None when trying to access a frozen set with a non-hashable index.
        
        This test verifies that deep_find handles attempts to access a frozen set
        using a non-hashable value (like a list) as the index. Since frozen sets
        can only contain hashable values, any attempt to use a non-hashable value
        as an index should return None.
        
        Expected: deep_find(frozenset((1, 2, 3)), '[]') -> None
        """
        data = frozenset((1, 2, 3))
        result = deep_find(data, '[]')
        self.assertEqual(result, None)

    def test_first_value_of_embedded_frozen_set(self):
        """
        Test that deep_find can access the first value of a frozen set nested within a dictionary.
        
        This test verifies that deep_find can access elements in a frozen set that
        is embedded within a dictionary structure. It tests the ability to traverse
        through a dictionary to reach a frozen set and then access its elements.
        
        Expected: deep_find({'values': frozenset((1, 2, 3))}, 'values.0') -> 1
        """
        data: dict = {
            'values': frozenset((1, 2, 3)),
        }
        result = deep_find(data, 'values.0')
        self.assertEqual(result, 1)

    def test_all_values_of_frozen_set(self):
        """
        Test that deep_find can retrieve all values from a frozen set using the wildcard operator.
        
        This test verifies that deep_find can use the wildcard operator (*) to
        retrieve all values from a frozen set that is embedded within a dictionary.
        It tests the ability to access all elements of a frozen set in a single
        operation.
        
        Expected: deep_find({'values': frozenset((1, 2, 3))}, 'values.*') -> [1, 2, 3]
        """
        data: dict = {
            'values': frozenset((1, 2, 3)),
        }
        result = deep_find(data, 'values.*')
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
