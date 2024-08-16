from object_case_switcher import transform_structure

@transform_structure(_async=False, case_type="camelToSnake")
def some_function():
    return {
        "asdgAsdf": 42,
    }

print(some_function())