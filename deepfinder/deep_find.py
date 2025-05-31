from __future__ import annotations

from typing import Any, Iterable


def deep_find(
    obj: Any,
    path: str,
    path_token: str = '.',
    default: Any = None,
) -> Any:
    """
    Find a value in a nested structure using a dot-notation path.

    This function allows you to access nested values in dictionaries, lists, and objects
    using a simple dot-notation path string. It supports special operators like '*', '?',
    and '*?' for advanced searching capabilities.

    Args:
        obj: The object to search in. Can be a dictionary, list, or any object with attributes.
        path: The path to the desired value using dot notation (e.g., 'users.0.name').
        path_token: The character used to separate path segments (default: '.').
        default: The value to return if the path is not found or raises an error (default: None).

    Returns:
        The found value or the default value if not found.

    Examples:
        >>> data = {'users': [{'name': 'John'}, {'name': 'Jane'}]}
        >>> deep_find(data, 'users.0.name')
        'John'
        >>> deep_find(data, 'users.*.name')
        ['John', 'Jane']
    """
    path = path.split(path_token)
    if path == ['']:
        path = None
    result = _rec_helper(obj, path)

    if result is not None:
        return result

    return default


def _rec_helper(obj: Any, path: list[str]) -> Any:
    """
    Recursive helper function to traverse the object structure.

    This function handles the actual traversal of the object structure, supporting
    dictionaries, lists, and objects with attributes.

    Args:
        obj: The current object being traversed.
        path: List of path segments remaining to traverse.

    Returns:
        The found value or None if not found.
    """
    if not path:
        return obj

    current_path = path.pop(0)

    if isinstance(obj, dict):
        return _rec_helper(obj.get(current_path), path)

    if isinstance(obj, Iterable) and not isinstance(obj, str):
        obj = list(obj)

    if isinstance(obj, list):
        return _rec_list_helper(obj, path, current_path)

    if hasattr(obj, '__dict__') and current_path in vars(obj):
        return _rec_helper(vars(obj)[current_path], path)
    
    return


def _rec_list_helper(obj: list[Any], path: list[str], current_path: str):
    """
    Helper function to handle list traversal with special operators.

    This function handles the traversal of lists with support for special operators:
    - '*': Get all items
    - '?': Get first non-null value
    - '*?': Get all non-null values

    Args:
        obj: The list to traverse.
        path: List of path segments remaining to traverse.
        current_path: The current path segment being processed.

    Returns:
        The found value(s) or None if not found.

    Examples:
        >>> data = [{'name': 'John'}, {'name': 'Jane'}]
        >>> _rec_list_helper(data, ['name'], '*')
        ['John', 'Jane']
        >>> _rec_list_helper(data, ['age'], '?')
        None
    """
    if current_path == '*':
        return [_rec_helper(sub_obj, path.copy()) for sub_obj in obj]

    if current_path in ['*?', '?*']:
        with_nones_results = [_rec_helper(sub_obj, path.copy()) for sub_obj in obj]
        clear_results = [obj for obj in with_nones_results if obj is not None]
        return clear_results

    if current_path == '?':
        for sub_obj in obj:
            result = _rec_helper(sub_obj, path.copy())
            if result is not None:
                return result
        return

    try:
        current_path_index = int(current_path)
    except ValueError as _:
        return
    if current_path_index >= len(obj):
        return
    return _rec_helper(obj[current_path_index], path)
