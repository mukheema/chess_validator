#!/usr/bin/env python3 -tu


import json
import requests


class ChessClient:
    def __init__(self, url):
            self._url = url

    def MakeMove(self, userParams):
        payload = {
            "jsonrpc": "2.0",
            "method": "MakeMove",
            "params": userParams,
            "id": 1
        }
        headers = {'content-type': 'application/json'}

        userResponse = requests.post(self._url, data=userParams, headers=headers).json()
        return userResponse.values()

    def XX_Method(self, userParams):
        raise NotImplementedError
