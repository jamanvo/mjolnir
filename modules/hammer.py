# -*- coding: utf-8 -*-
import requests
import json


# start to compare
def smash(url, params, ctrl, method):
    args = json.loads(params) if params != '' else {}

    # control data parse
    ctrl = json.loads(ctrl)

    # call api
    response = call_api(url, args, method)
    # set api response to experiment group
    exp = response_parser(response)

    result = call_thunder(ctrl, exp, response)

    return result


# call api
def call_api(url, params, method):
    request = api_method(method)
    res = requests.Response()

    if method == 'POST':
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        res = request(url, data=params, headers=headers)
    elif method == 'GET':
        res = request(url, params=params)

    # except - res is None
    return res


def response_parser(response: requests.Response):
    # except - response is None or not requests.Response
    try:
        return response.json()
    except json.decoder.JSONDecodeError:
        return None


def api_method(method):
    return requests.post if method == 'post' else requests.get


def call_thunder(ctrl, exp, response):
    ctrl_group = parse_response_type(ctrl)
    exp_group = parse_response_type(exp)
    compare_result = compare_responses(ctrl_group, exp_group)

    result = {
        "result": {
            "api_result": response.json(),
            "status_code": response.status_code,
            "parsed_ctrl": type_to_string(ctrl_group),
            "parsed_exp": type_to_string(exp_group),
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
                print(ctrl, exp);
                result[key] = compare_type(ctrl[key], exp[key])
    else:
        result = compare_type(ctrl, exp)

    return [result] if res_type == list else result


def type_to_string(dic):
    result = {}
    res_type = type(dic)

    print(dic)
    if res_type == list:
        dic = dic[0]

    if dic == dict:
        keys = dic.keys()

        for key in keys:
            if dic[key] == list or dic[key] == dict:
                result[key] = parse_response_type(dic[key])
            else:
                result[key] = str(dic[key])
    else:
        result = str(dic)

    # response type setting
    return [result] if res_type == list else result
