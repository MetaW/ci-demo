# coding: utf-8

import unittest
from src.demo import *


class TestDemo(unittest.TestCase):
    def test_init(self):
        a = Demo()
        self.assertTrue(isinstance(a,Demo))

    def test_add(self):
        a = Demo()
        self.assertEqual(a.add(0,5),5)
        self.assertEqual(a.add(-5,20),15)
        self.assertEqual(a.add(3,8),11)

    def test_sub(self):
        a = Demo()
        self.assertEqual(a.sub(3,9),-6)
        self.assertEqual(a.sub(0,5),-5)

    def test_mul(self):
        a = Demo()
        self.assertEqual(a.mul(0,8),0)
        self.assertEqual(a.mul(-3,7),-21)
        self.assertEqual(a.mul(4,6),24)


if __name__ == '__main__':
    unittest.main()
