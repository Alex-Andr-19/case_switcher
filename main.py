import asyncio
from transformPropModule import transform_structure
from pprint import pprint

@transform_structure()
async def some_func():
# @transform_structure(_async=False)
# def some_func():
    return {
        "asdf_qwer_asdf_zxcv": {
            "asdf_cvz": 42
        },
        "asdf": [
            {
                "URL_link":"asdf",
                "asdf_qwerRE_ad": {
                    "qwer_asdf": [
                        {
                            "asdf": 1234,
                            "asdfAsdfRewq": 42,
                        }
                    ],
                }
            },
            {
                "URL_link":"asdf"
            },
            {
                "URL_link":"asdf"
            },
        ]
    }

async def print_func():
    pprint(await some_func())
asyncio.run(print_func())
    
# pprint(some_func())