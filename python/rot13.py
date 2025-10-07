"""ROT13 is a simple letter substitution cipher that replaces 
a letter with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, 
they should be returned as they are. Only letters from 
the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating."""

import unittest

class RotTest(unittest.TestCase):
    def test_rot(self):
        self.assertEqual(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
        self.assertEqual(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
        self.assertEqual(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')

def rot13(message):
    fro = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    to = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    result = ""
    for char in message:
        result += to[fro.index(char)] if char.isalpha() else char
    return result

unittest.main()

