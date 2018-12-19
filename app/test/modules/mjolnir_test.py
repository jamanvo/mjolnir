import json

from app.modules.mjolnir import Mjolnir, Hammer


# test dataset
json_string = '''
    {
        "result": { 
            "user": {
                "id": 1,
                "name": "jarvis"
            },
            "milecards": [
                {
                    "id": 2,
                    "current_mile": 1
                },
                {
                    "id": 3,
                    "current_mile": 1
                }
            ]
        }
    }
'''

res_json = json.dumps(json_string)

# test Mjolnir
# test __init__(url, response)
def test__init__():
    url = "test.com/test"
    response = {}
    Mjolnir.__init__()

# test _parse_response_type_(response)
def test_parse_response_type_():
    req = {"key": "val"}
    result = {"key": type("val")}

    assert Mjolnir._parse_response_type_(req) == result

