import unittest

from deepfinder import deep_find


class TestFindDefault(unittest.TestCase):
    def test_with_basic_dict(self):
        """
        Test that deep_find returns the specified default value when a key is not found in a dictionary.
        
        When searching for a non-existent key in a dictionary, deep_find should return
        the provided default value instead of None. This verifies the basic default
        value behavior for dictionary lookups.
        
        Expected: deep_find({'any': 'any'}, 'some', default='default') -> 'default'
        """
        data: dict = {'any': 'any'}
        result = deep_find(data, 'some', default='default')
        self.assertEqual(result, 'default')

    def test_with_list_and_find_all(self):
        """
        Test that deep_find returns a list of None values when using wildcard (*) on a list
        where no items match the path.
        
        When using the wildcard operator (*) to search through a list and no items
        match the specified path, deep_find should return a list containing None
        for each item in the original list. This verifies the default behavior
        for wildcard searches in lists.
        
        Expected: deep_find([{'any': 'any'}], '*.some', default='default') -> [None]
        """
        data: list = [{'any': 'any'}]
        result = deep_find(data, '*.some', default='default')
        self.assertEqual(result, [None])

    def test_with_list_and_find_all_without_nulls(self):
        """
        Test that deep_find returns an empty list when using wildcard with null filtering (*?)
        on a list where no items match the path.
        
        When using the wildcard with null filtering operator (*?) to search through
        a list and no items match the specified path, deep_find should return an
        empty list. This verifies that null values are properly filtered out
        when using the *? operator.
        
        Expected: deep_find([{'any': 'any'}], '?*.some', default='default') -> []
        """
        data: list = [{'any': 'any'}]
        result = deep_find(data, '?*.some', default='default')
        self.assertEqual(result, [])

    def test_with_list_and_find_some(self):
        """
        Test that deep_find returns the default value when using the first match operator (?)
        on a list where no items match the path.
        
        When using the first match operator (?) to search through a list and no
        items match the specified path, deep_find should return the provided
        default value. This verifies that the default value is properly returned
        when no matches are found using the ? operator.
        
        Expected: deep_find([{'any': 'any'}], '?.some', default='default') -> 'default'
        """
        data: list = [{'any': 'any'}]
        result = deep_find(data, '?.some', default='default')
        self.assertEqual(result, 'default')


if __name__ == '__main__':
    unittest.main()
