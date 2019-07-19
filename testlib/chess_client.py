#!/usr/bin/env python3 -tu


import json
import requests


class ChessClient:
    def __init__(self, url):
            self._url = url

    def MakeMove(self, userParams):
        userRequest = {
            "jsonrpc": "2.0",
            "method": "MakeMove",
            "params": userParams,
            "id": 1
        }
        userResponse = requests.post(self._url, data=json.dumps(userRequest))
        return userResponse

    def XX_Method(self, userParams):
            return "Not Implemented"
