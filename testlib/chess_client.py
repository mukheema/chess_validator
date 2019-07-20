#!/usr/bin/env python3 -tu

import json
import requests


class ChessClient:
    def __init__(self, url):
            self._url = url

    def MakeMove(self, userParams):
        payload = {
            "method": "MakeMove",
            "params": userParams,
            "id": 1,
            "jsonrpc": "2.0"
        }
        headers = {'content-type': 'application/json'}

        #userResponse = requests.post(str(self._url), data=payload, headers=headers).json()
        userResponse = requests.post('http://chesstest.solidfire.net:8080/json-rpc', data=payload, headers={'content-type': 'application/json'}).json()
        print("ChessBoard Response : %s" % userResponse.values())
        print("ChessBoard Response : %s" % userResponse.values())
        return userResponse.values()

    def XX_Method(self, userParams):
        raise NotImplementedError
