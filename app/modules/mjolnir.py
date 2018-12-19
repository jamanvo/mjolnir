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
            self.response = self._parse_response_type_(response)
        except AttributeError:
            print(traceback.format_exc())

    def _parse_response_type_(self, response):
        result = {}
        keys = response.keys()
        for key in keys:
            if isinstance(response[key], list) or isinstance(response[key], dict):
                result[key] = self._parse_response_type_(response[key])
            else:
                result[key] = type(response[key])

        # response type setting
        return result


class Hammer:
    @staticmethod
    def compare_type(ctrl, exp):
        result = {}
        exp_keys = exp.keys()

        for ek in exp_keys:
            try:
                if isinstance(exp[ek], type(ctrl[ek])):
                    result[ek] = True
                else:
                    result[ek] = False
            except KeyError:
                result[ek] = None
