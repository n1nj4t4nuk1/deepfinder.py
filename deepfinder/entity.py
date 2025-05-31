import builtins

from deepfinder import deep_find


class DeepFinderList(list):
    """
    A list subclass that adds deep finding capabilities.

    This class extends Python's built-in list type to add the ability to search
    through nested structures using dot notation. It inherits all list functionality
    while adding the deep_find method.

    Examples:
        >>> pokemons = DeepFinderList([
        ...     {'name': 'pikachu', 'type': 'electric'},
        ...     {'name': 'charmander', 'type': 'fire'}
        ... ])
        >>> pokemons.deep_find('*.name')
        ['pikachu', 'charmander']
    """

    def deep_find(self, path: str):
        """
        Find values in the list using dot notation.

        Args:
            path: The path to search for using dot notation (e.g., '*.name').

        Returns:
            The found value(s) or None if not found.

        Examples:
            >>> pokemons = DeepFinderList([{'name': 'pikachu'}])
            >>> pokemons.deep_find('0.name')
            'pikachu'
        """
        return deep_find(self, path)


class DeepFinderDict(dict):
    """
    A dictionary subclass that adds deep finding capabilities.

    This class extends Python's built-in dict type to add the ability to search
    through nested structures using dot notation. It inherits all dictionary
    functionality while adding the deep_find method.

    Examples:
        >>> user = DeepFinderDict({
        ...     'name': 'ash',
        ...     'pokemons': [
        ...         {'name': 'pikachu'},
        ...         {'name': 'charmander'}
        ...     ]
        ... })
        >>> user.deep_find('pokemons.*.name')
        ['pikachu', 'charmander']
    """

    def deep_find(self, path: str):
        """
        Find values in the dictionary using dot notation.

        Args:
            path: The path to search for using dot notation (e.g., 'user.profile.name').

        Returns:
            The found value(s) or None if not found.

        Examples:
            >>> user = DeepFinderDict({'name': 'ash'})
            >>> user.deep_find('name')
            'ash'
        """
        return deep_find(self, path)


def nativify():
    """
    Replace Python's built-in list and dict types with DeepFinder versions.

    This function modifies Python's builtins to replace the standard list and dict
    types with DeepFinderList and DeepFinderDict respectively. This means all
    lists and dictionaries created after calling this function will have deep
    finding capabilities by default.

    Warning:
        This is a global change that affects the entire Python runtime.
        Use with caution as it may affect other libraries that expect
        standard list and dict behavior.

    Examples:
        >>> nativify()
        >>> my_list = [{'name': 'pikachu'}]
        >>> my_list.deep_find('0.name')  # Now works on standard lists
        'pikachu'
    """
    builtins.list = DeepFinderList
    builtins.dict = DeepFinderDict
