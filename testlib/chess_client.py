#!/usr/bin/env python3 -tu

import json
import requests


class ChessClient:
    def __init__(self, url):
            self._url = url

    def MakeMove(self, userParams=None):
        if not userParams:
            userParams = {}
        payload = {
            "method": "MakeMove",
            "params": userParams,
            "id": 1,
            "jsonrpc": "2.0"
        }
        headers = {'content-type': 'application/json'}

        print("User Request: %s" % payload)
        userResponse = requests.post(str(self._url), data=json.dumps(payload), headers=headers).json()
        print("ChessBoard Response: %s" % userResponse.values())
        return userResponse.values()

    def XX_Method(self, userParams):
        raise NotImplementedError
