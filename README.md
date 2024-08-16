# CASE SWITCHER
The easiest way to switch case of prop in return of your functions

## Installing
```bash
pip install object_case_switcher
```

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