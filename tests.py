import unittest
from dec2bin import dec2bin
from bin2dec import bin2dec

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

    def testbin2dec(self):
        self.assertFalse(bin2dec(''))
        self.assertEqual(bin2dec('0'),0)
        self.assertEqual(bin2dec('1'),1)
        self.assertEqual(bin2dec('10'),2)
        self.assertEqual(bin2dec('11'),3)

        self.assertEqual(bin2dec('1000'),8)
        self.assertEqual(bin2dec('100001'),33)
        self.assertEqual(bin2dec('111001'),57)
        self.assertEqual(bin2dec('1011110'),94)

        self.assertEqual(bin2dec('00000000'),0)
        self.assertEqual(bin2dec('01'),1)
        self.assertEqual(bin2dec('011'),3)
        self.assertEqual(bin2dec('00000111'),7)
        self.assertEqual(bin2dec('000001111'),15)
        self.assertEqual(bin2dec('000001111'),15)

        self.assertEqual(bin2dec('0001101000110101001'),53673)
        self.assertEqual(bin2dec('010101101001010100'), 88660)

if __name__ == '__main__':
    unittest.main
