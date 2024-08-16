# CASE SWITCHER
The easiest way to switch case of prop in return of your functions

## Installing
```bash
pip install object_case_switcher
```

## Examples
Simple use
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