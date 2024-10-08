# CASE SWITCHER

This module provides a very **useful** feature that will simplify communication between developers of Python RestAPI and other API libraries and frontend developers.

The provided function (`transform_structure`) makes it possible to develop the main function code on the usual code case, but, called by default, it converts the fields of the object returned by the main function from `snake_case` to `camelCase`.

> It is better to install this library in your virtual environment

## Installing
```bash
pip install object_case_switcher
```

## Syntax
```python
@transform_structure()
async def load_data(*args, **kwargs):
    ...
```

## Parameters
- `case_type` - Type of transform rule (`snakeToCamel`, `camelToSnake`). Defaults to "snakeToCamel"  

- `transform_for` - Target of executon transform (return, argument). Defaults to "return"

- `arg_index` - Index of argument of target function. Defaults to **0**

- `arg_name` - Name of argument of target function. Defaults to **""**

- `_async` - Is synchronus or asynchronus target function . Defaults to `True`

## Examples
### Simple use
```python
from object_case_switcher import transform_structure

@transform_structure(_async=False)
def some_function():
    return {
        "some_property": 42,
    }

print(some_function())

# >>> '{"someProperty": 42}'
```

### Recursive case
You can return an object with any level of nesting from a function
```python
from object_case_switcher import transform_structure

@transform_structure(_async=False)
def some_function():
    return {
        "some_property": 42,
        "some_other_property": {
            "a": 52,
            "b": [
                {
                    "title_name": "John",
                },
                {
                    "title_name": "Dow",
                },
            ]
        },
    }

print(some_function())

```
Output
```json
{
    "someProperty": 42,
    "someOtherProperty": {
        "a": 52,
        "b": [
            {"titleName": "John"},
            {"titleName": "Dow"},
        ]
    }
}
```