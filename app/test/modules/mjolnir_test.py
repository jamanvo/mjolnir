import json

from app.modules.mjolnir import Mjolnir


# test dataset
ctrl_dict = {
                "result": {
                    "user": {
                        "id": int,
                        "name": str
                    },
                    "milecards": [
                        {
                            "id": int,
                            "current_mile": int
                        }
                    ]
                }
            }

exp_json = '''
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

exp_dict = json.loads(exp_json)


# test Mjolnir
# test _parse_response_type_(response)
def test_compare_type():
    ctrl = 1
    exp = 2

    assert Mjolnir._compare_type(ctrl, exp) is True


def test_parse_response_type():
    result = Mjolnir._parse_response_type(exp_dict)

    assert result == ctrl_dict
