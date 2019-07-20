#!/usr/bin/env python3 -tu

import os
import sys
import json
import unittest


ProjectPath = os.path.realpath(__file__) + "../"

print(ProjectPath)

sys.path.append("/Users/mukheema/aDisk/my_proj/chess_validator")
from testlib.chess_client import *

class Positivetest_s(unittest.TestCase):
    """
       Validate Positive functional tests
    """

    def setUp(self):
        """ pass url to test"""
        self.testClient = ChessClient("http://chesstest.solidfire.net:8080/")
#        print("Starting Chess Board Test Setup")

    def test_1(self):
        print("Testcase1 stared\n")
#        inputRequest = '{ "method": "MakeMove", "params": { "boardState": [{"loc": "a8", "type": "r"}, {"loc": "b8", "type": "n"}, {"loc": "c8", "type": "b"},{"loc": "d8", "type": "q"}, {"loc": "e8", "type": "k"}, {"loc": "f8", "type": "b"}, {"loc": "g8", "type":"n"}, {"loc": "h8", "type": "r"}, {"loc": "a7", "type": "p"}, {"loc": "b7", "type": "p"}, {"loc": "c7","type": "p"}, {"loc": "d7", "type": "p"}, {"loc": "e7", "type": "p"}, {"loc": "f7", "type": "p"}, {"loc":"g7", "type": "p"}, {"loc": "h7", "type": "p"}, {"loc": "a1", "type": "R"}, {"loc": "b1", "type": "N"},{"loc": "c1", "type": "B"}, {"loc": "d1", "type": "Q"}, {"loc": "f1", "type": "B"}, {"loc": "g1", "type":"N"}, {"loc": "h1", "type": "R"}, {"loc": "a2", "type": "P"}, {"loc": "b2", "type": "P"}, {"loc": "c2","type": "P"}, {"loc": "d2", "type": "P"}, {"loc": "e2", "type": "P"}, {"loc": "f2", "type": "P"}, {"loc":"g2", "type": "P"}, {"loc": "e1", "type": "K"}, {"loc": "h2", "type": "P"}],"move": "Nc5","playerState": "w"}, "id": 1,"jsonrpc": "2.0"}'
        inputRequest = { "boardState": [ {"loc": "a8", "type": "r"}, {"loc": "b8", "type": "n"}, {"loc": "c8", "type": "b"}, {"loc": "d8", "type": "q"}, {"loc": "e8", "type": "k"}, {"loc": "f8", "type": "b"}, {"loc": "g8", "type": "n"}, {"loc": "h8", "type": "r"}, {"loc": "a7", "type": "p"}, {"loc": "b7", "type": "p"}, {"loc": "c7", "type": "p"}, {"loc": "d7", "type": "p"}, {"loc": "e7", "type": "p"}, {"loc": "f7", "type": "p"}, {"loc": "g7", "type": "p"}, {"loc": "h7", "type": "p"}, {"loc": "a1", "type": "R"}, {"loc": "b1", "type": "N"}, {"loc": "c1", "type": "B"}, {"loc": "d1", "type": "Q"}, {"loc": "f1", "type": "B"}, {"loc": "g1", "type": "N"}, {"loc": "h1", "type": "R"}, {"loc": "a2", "type": "P"}, {"loc": "b2", "type": "P"}, {"loc": "c2", "type": "P"}, {"loc": "d2", "type": "P"}, {"loc": "e2", "type": "P"}, {"loc": "f2", "type": "P"}, {"loc": "g2", "type": "P"}, {"loc": "e1", "type": "K"}, {"loc": "h2", "type": "P"}], "move": "Nc3", "playerState": "w" }

        expectResponse = {
            "boardState": [
                    {"loc": "a1", "type": "R"}, {"loc": "c1", "type": "B"}, {"loc": "d1", "type": "Q"},
                    {"loc": "e1", "type": "K"}, {"loc": "f1", "type": "B"}, {"loc": "g1", "type": "N"},
                    {"loc": "h1", "type": "R"}, {"loc": "a2", "type": "P"}, {"loc": "b2", "type": "P"},
                    {"loc": "c2", "type": "P"}, {"loc": "d2", "type": "P"}, {"loc": "e2", "type": "P"},
                    {"loc": "f2", "type": "P"}, {"loc": "g2", "type": "P"}, {"loc": "h2", "type": "P"},
                    {"loc": "c3", "type": "N"}, {"loc": "a7", "type": "p"}, {"loc": "b7", "type": "p"},
                    {"loc": "c7", "type": "p"}, {"loc": "d7", "type": "p"}, {"loc": "e7", "type": "p"},
                    {"loc": "f7", "type": "p"}, {"loc": "g7", "type": "p"}, {"loc": "h7", "type": "p"},
                    {"loc": "a8", "type": "r"}, {"loc": "b8", "type": "n"}, {"loc": "c8", "type": "b"},
                    {"loc": "d8", "type": "q"}, {"loc": "e8", "type": "k"}, {"loc": "f8", "type": "b"},
                    {"loc": "g8", "type": "n"}, {"loc": "h8", "type": "r"}],
            "playerState": "b",
            "gameState": ""
            }
        testResponse = self.testClient.MakeMove(inputRequest)
        self.assertEqual(expectResponse, testResponse, "Failed to get expected response")

        print("test_1 validate Passed")
        print("Testcase1 done\n")


    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass



if __name__ == '__main__':
    unittest.main()
