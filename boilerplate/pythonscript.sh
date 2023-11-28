#!/bin/bash

filename='changeme.py'

echo "import unittest

class Solution:
    def your_solution(self):
        pass

class Yourtest(unittest.TestCase):
    def test_yourtest(self):
        pass

if __name__ == '__main__':
    unittest.main()
" > $filename

echo "created python boiler plate"
