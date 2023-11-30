'''
a palindome validator
'''
import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        fore = 0
        end = len(s) - 1
        while fore < end:
            if not s[fore].isalnum():
                fore += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[fore].lower() == s[end].lower():
                fore += 1
                end -= 1
            else:
                return False

        return True


class TestPalindome(unittest.TestCase):
    def test_palindome_validatore(self):

        input1 = "A man, a plan, a canal: Panama"
        input2 = "race a car"
        input3 = " "

        output1 = Solution.isPalindrome(self, input1)
        output2 = Solution.isPalindrome(self, input2)
        output3 = Solution.isPalindrome(self, input3)
        self.assertEqual(True, output1)
        self.assertEqual(False, output2)
        self.assertEqual(True, output3)


if __name__ == '__main__':
    unittest.main()