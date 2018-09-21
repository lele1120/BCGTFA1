# coding:utf-8
import unittest


class TestCasePrint(unittest.TestCase):

    def assertEqual(self, first, second, msg=None):
        print("\n")
        print("Actual:")
        print(first)
        print("Expect:")
        print(second)

        assertion_func = self._getAssertEqualityFunc(first, second)
        assertion_func(first, second, msg=msg)




