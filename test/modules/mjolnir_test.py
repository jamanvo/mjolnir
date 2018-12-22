import json

from modules import hammer

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

result_dict = {
            "result": {
                "user": {
                    "id": True,
                    "name": True
                },
                "milecards": [
                    {
                        "id": True,
                        "current_mile": True
                    }
                ]
            }
        }

exp_dict = json.loads(exp_json)


# test Mjolnir

# test _parse_response_type_(response)
def test_compare_type():
    ctrl = 1
    exp = 2

    assert hammer.compare_type(ctrl, exp) is True


def test_parse_response_type():
    result = hammer.parse_response_type(exp_dict)

    assert result == ctrl_dict


def test_compare_response():
    exp = hammer.parse_response_type(exp_dict)
    result = hammer.compare_responses(ctrl_dict, exp)

    assert result == result_dict


def test_api_method():
    method = 'post'
    request = hammer.api_method(method)

    assert callable(request) is True


def test_api_call():
    # get
    url = 'http://localhost:5000/health_check'
    method = 'get'
    params = {'body': 'test'}

    res = hammer.call_api(url, params, method)

    assert res.status_code == 200

    # post
    method = 'post'

    res = hammer.call_api(url, params, method)

    assert res.status_code == 200
    assert res.json()['body'] is not None
