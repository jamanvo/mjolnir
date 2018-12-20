# -*- coding: utf-8 -*-
import requests


# start to compare
def smash(url, ctrl):
    return

# call api
def call_api(url, params):
    return

def call_thunder(ctrl, exp):
    ctrl_group = parse_response_type(ctrl)
    exp_group = parse_response_type(exp)
    compare_result = compare_responses(ctrl_group, exp_group)

    result = {
        "result": {
            "parsed_ctrl": ctrl_group,
            "parsed_exp": exp_group,
            "compare_result": compare_result
        }
    }

    return result

def parse_response_type(response):
    result = {}
    res_type = type(response)

    if res_type == list:
        response = response[0]

    if isinstance(response, dict):
        keys = response.keys()

        for key in keys:
            if isinstance(response[key], list) or isinstance(response[key], dict):
                result[key] = parse_response_type(response[key])
            else:
                result[key] = type(response[key])
    else:
        result = type(response)

    # response type setting
    return [result] if res_type == list else result

def compare_type(ctrl, exp):
    return type(ctrl) == type(exp)

def compare_responses(ctrl, exp):
    result = {}
    res_type = type(ctrl)

    if res_type == list:
        ctrl = ctrl[0]
        exp = exp[0]

    if isinstance(ctrl, dict):
        keys = ctrl.keys()

        for key in keys:
            if isinstance(ctrl[key], list) or isinstance(ctrl[key], dict):
                result[key] = compare_responses(ctrl[key], exp[key])
            else:
                result[key] = compare_type(ctrl[key], exp[key])
    else:
        result = compare_type(ctrl, exp)

    return [result] if res_type == list else result
