<h1 align="center">🔍 Deepfinder </h1>

<div align="center">

![](https://img.shields.io/badge/PRs-welcome-green.svg)
[![GitHub](https://img.shields.io/github/license/jparadadev/deepfinder.py)](https://github.com/jparadadev/deepfinder.py/blob/main/LICENSE)
[![Pypi](https://img.shields.io/pypi/v/deepfinder)](https://pypi.org/project/deepfinder/)
[![Downloads](https://pepy.tech/badge/deepfinder)](https://pepy.tech/project/deepfinder)
[![GA](https://github.com/jparadadev/deepfinder.py/workflows/Tests/badge.svg)](https://github.com/jparadadev/deepfinder.py/actions/workflows/test.yml)
  
</div>

![](https://raw.githubusercontent.com/jparadadev/deepfinder.py/assets/assets/logo.png)

Search attributes easily using dot paths. Within structures of type dictionary, list and embedded substructures with simple format 'dict.users.0.name'.

## Getting Started

### Installation

```Shell
  pip install deepfinder
```

### Usage

#### Basic sample

```python
from deepfinder import deep_find
user: dict = {
    'name': 'ash',
    'links': {
        'pokehub': '@ash'
    },
}
print(deep_find(user, 'links.pokehub'))
# output: '@ash'
```

#### List sample

```python
from deepfinder import deep_find
user: dict = {
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
print(deep_find(user, 'pokemons.0.name'))
# output: 'pikachu'
```

#### List all result sample

```python
from deepfinder import deep_find
user: dict = {
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
print(deep_find(user, 'pokemons.*.name'))
# output: ['pikachu', 'charmander']
```

#### Find the first non-null result

```python
from deepfinder import deep_find
user: dict = {
    'name': 'ash',
    'pokemons': [
        {
            'name': 'pikachu',
        },
        {
            'name': 'charmander',
            'ball': 'superball'
        }
    ]
}
print(deep_find(user, 'pokemons.?.ball'))
# output: 'superball'
```

#### Find all non-null results

```python
from deepfinder import deep_find
user: dict = {
    'name': 'ash',
    'pokemons': [
        {
            'name': 'pikachu',
        },
        {
            'name': 'charmander',
            'ball': 'superball'
        },
        {
            'name': 'lucario',
            'ball': 'ultraball'
        }
    ]
}
print(deep_find(user, 'pokemons.*?.ball'))
# output: ['superball', 'ultraball']
```



### Use custom dict and list

```python
from deepfinder.entity import DeepFinderDict
user: dict = DeepFinderDict({
    'name': 'ash',
    'pokemons': [
        {
            'name': 'pikachu'
        },
        {
            'name': 'charmander',
            'ball': 'superball'
        }
    ]
})
print(user.deep_find('pokemons.?.ball'))
# output: 'superball'
```

```python
from deepfinder.entity import DeepFinderList
users: list = DeepFinderList([{
    'name': 'ash',
    'pokemons': [
        {
            'name': 'pikachu'
        }, 
        {
            'name': 'charmander',
            'ball': 'superball'
        }
    ]
}])
print(users.deep_find('0.pokemons.?.ball'))
# output: 'superball'
```
