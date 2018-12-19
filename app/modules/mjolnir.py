# -*- coding: utf-8 -*-
import traceback


class Mjolnir:
    url = None
    key = None
    response = None

    def __init__(self, url, response):
        try:
            self.url = url
            self.key = url.split('/')[-1]
            self.response = self._parse_response_type(response)
        except AttributeError:
            print(traceback.format_exc())

    @staticmethod
    def _parse_response_type(response):
        result = {}
        res_type = response

        if isinstance(res_type, list):
            response = response[0]

        keys = response.keys()

        for key in keys:
            if isinstance(response[key], list) or isinstance(response[key], dict):
                result[key] = Mjolnir._parse_response_type(response[key])
            else:
                result[key] = type(response[key])

        # response type setting
        return [result] if isinstance(res_type, list) else result

    @staticmethod
    def _compare_type(ctrl, exp):
        return type(ctrl) == type(exp)
