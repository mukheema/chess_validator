#!/usr/bin/env python3 -tu

#import json
#from jsonrpc2 import JsonRpcApplication
#from webtest import TestApp
from jsonrpclib import Server

class ChessClient:
    def __init__(self, url):
        self._client = Server(url)

    def MakeMove(self, userParams):
        self._client.MakeMove(userParams)

def MakeMove(userParams):
    return
def MakeMove(userParams):
    request = {
        "method": "MakeMove",
        "params": userParams,
        "id": 1,
        "jsonrpc": "2.0"
        }
    app = ChessClient(request) 

    testApp = TestApp(app)
    call_values = { 'jsonrpc': '2.0', 'method': 'MakeMove', 'id': 1}
    return testapp.post('/'. params=json.dumps(call_values), content_type="application/json")
