# 🔍 Deepfinder

[![GitHub](https://img.shields.io/github/license/n1nj4t4nuk1/deepfinder.py)](https://github.com/n1nj4t4nuk1/deepfinder.py/blob/main/LICENSE)
[![Pypi](https://img.shields.io/pypi/v/deepfinder)](https://pypi.org/project/deepfinder/)
[![Downloads](https://pepy.tech/badge/deepfinder)](https://pepy.tech/project/deepfinder)
[![GA](https://github.com/n1nj4t4nuk1/deepfinder.py/workflows/Tests/badge.svg)](https://github.com/n1nj4t4nuk1/deepfinder.py/actions/workflows/test.yml)

![](https://raw.githubusercontent.com/n1nj4t4nuk1/deepfinder.py/assets/assets/logo.png)

## What is Deepfinder?

Deepfinder is a Python library that makes it easy to access nested data in dictionaries and lists using simple dot notation. Instead of writing complex nested dictionary access code, you can use intuitive paths like `'users.0.name'` to get the data you need.

## Installation

```bash
pip install deepfinder
```

## Quick Start

### Basic Usage

```python
from deepfinder import deep_find

# Example data
user = {
    'name': 'ash',
    'links': {
        'pokehub': '@ash'
    }
}

# Get the pokehub link
result = deep_find(user, 'links.pokehub')
print(result)  # Output: '@ash'
```

### Working with Lists

```python
from deepfinder import deep_find

# Example data with a list of pokemon
user = {
    'name': 'ash',
    'pokemons': [
        {
            'name': 'pikachu',
            'type': 'electric'
        },
        {
            'name': 'charmander',
            'type': 'fire'
        }
    ]
}

# Get pikachu's name (first pokemon)
result = deep_find(user, 'pokemons.0.name')
print(result)  # Output: 'pikachu'

# Get all pokemon names
result = deep_find(user, 'pokemons.*.name')
print(result)  # Output: ['pikachu', 'charmander']
```

## Advanced Features

### Finding First Non-Null Value

Use `?` to get the first non-null value in a list:

```python
user = {
    'pokemons': [
        {'name': 'pikachu'},  # no ball
        {'name': 'charmander', 'ball': 'superball'},  # has ball
        {'name': 'lucario', 'ball': 'ultraball'}  # has ball
    ]
}

# Get the first pokemon that has a ball
result = deep_find(user, 'pokemons.?.ball')
print(result)  # Output: 'superball'
```

### Finding All Non-Null Values

Use `*?` to get all non-null values in a list:

```python
user = {
    'pokemons': [
        {'name': 'pikachu'},  # no ball
        {'name': 'charmander', 'ball': 'superball'},  # has ball
        {'name': 'lucario', 'ball': 'ultraball'}  # has ball
    ]
}

# Get all pokemon balls
result = deep_find(user, 'pokemons.*?.ball')
print(result)  # Output: ['superball', 'ultraball']
```

## Using Custom Classes

Deepfinder provides custom classes that make it even easier to work with nested data:

### DeepFinderDict

```python
from deepfinder.entity import DeepFinderDict

# Create a dictionary with built-in deep finding
user = DeepFinderDict({
    'name': 'ash',
    'pokemons': [
        {'name': 'pikachu'},
        {'name': 'charmander', 'ball': 'superball'}
    ]
})

# Use the deep_find method directly on the dictionary
result = user.deep_find('pokemons.?.ball')
print(result)  # Output: 'superball'
```

### DeepFinderList

```python
from deepfinder.entity import DeepFinderList

# Create a list with built-in deep finding
users = DeepFinderList([{
    'name': 'ash',
    'pokemons': [
        {'name': 'pikachu'},
        {'name': 'charmander', 'ball': 'superball'}
    ]
}])

# Use the deep_find method directly on the list
result = users.deep_find('0.pokemons.?.ball')
print(result)  # Output: 'superball'
```

## Path Syntax Reference

- `.` - Access dictionary keys
- `0`, `1`, etc. - Access list items by index
- `*` - Get all items in a list
- `?` - Get first non-null value
- `*?` - Get all non-null values

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
