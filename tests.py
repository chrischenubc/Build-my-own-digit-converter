import unittest
from dec2bin import dec2bin

class TestCases(unittest.TestCase):
    def testdec2bin(self):
        self.assertEqual(dec2bin(0),'0')
        self.assertEqual(dec2bin(1),'1')
        self.assertEqual(dec2bin(2),'10')
        self.assertEqual(dec2bin(3),'11')
        self.assertEqual(dec2bin(4),'100')
        self.assertEqual(dec2bin(7),'111')
        self.assertEqual(dec2bin(9),'1001')
        self.assertEqual(dec2bin(9),'1001')
        self.assertEqual(dec2bin(9),'1001')

        self.assertEqual(dec2bin(32),'100000')
        self.assertEqual(dec2bin(57),'111001')
        self.assertEqual(dec2bin(94),'1011110')
        self.assertEqual(dec2bin(99),'1100011')

if __name__ == '__main__':
    unittest.main
