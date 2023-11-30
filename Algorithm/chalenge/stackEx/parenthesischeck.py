import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '{([':
                stack.append(c)
            elif c in '})]':
                if stack == [] :
                    return False
                if c == '}' and stack[-1] == '{':
                    stack.pop(-1)
                elif c == ')' and stack[-1] == '(':
                    stack.pop(-1)
                elif c == ']' and stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False

        if stack == []:
            return True
        else:
            return False

class Yourtest(unittest.TestCase):
    def test_yourtest(self):
        s = ['()', '()[]{}', '(]','(])']

        output1 = Solution.isValid(self,s[0])
        output2 = Solution.isValid(self,s[1])
        output3 = Solution.isValid(self,s[2])
        output4 = Solution.isValid(self,s[3])

        self.assertEqual(output1,True)
        self.assertEqual(output2,True)
        self.assertEqual(output3,False)
        self.assertEqual(output4,False)

if __name__ == '__main__':
    unittest.main()

