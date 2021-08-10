#!/usr/bin/python

import unittest
from password_gen import *

class Test(unittest.TestCase):
    def test_case_1(self):
        test_pass = "thispasswordshouldpass"
        self.assertEqual(check_password(test_pass), True)
    def test_case_2(self):
        test_pass = "aaaTest"
        self.assertEqual(check_password(test_pass), False)
    def test_case_3(self):
        test_pass = "Testaaa"
        self.assertEqual(check_password(test_pass), False)
    def test_case_4(self):
        test_pass = "TestaaaTest"
        self.assertEqual(check_password(test_pass), False)
    def test_case_5(self):
        test_pass = "soc123cer"
        self.assertEqual(check_password(test_pass), False)
    def test_case_6(self):
        test_pass = "soccerxyz"
        self.assertEqual(check_password(test_pass), False)
    def test_case_7(self):
        test_pass = "iloveyou"
        self.assertEqual(check_password(test_pass), False)

if __name__ == "__main__":
    unittest.main()

