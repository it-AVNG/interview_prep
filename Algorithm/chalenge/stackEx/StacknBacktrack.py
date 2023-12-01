'''
input a number of parenthesis pairs.
output all the possible combination of the pairs
'''

import unittest

class Solution:
    def generateparenthesis(self,n: int) -> list:
        # valid case: when the open_count == close_count == n
        # only add open parenthesis when open_count <n
        # only add close parenthesis when close_count < open_count

        res = []
        stack = []

        def backtrack(open_count,close_count):

            #base case
            if open_count == close_count == n:
                res.append(''.join(stack))
                return

            # append open case
            if open_count <n:
                stack.append('(')
                backtrack(open_count+1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(')')
                backtrack(open_count, close_count+1)
                stack.pop()


        backtrack(0, 0)

        return res

class Yourtest(unittest.TestCase):
    def test_yourtest(self):
        input = [3, 1]
        out1 = Solution.generateparenthesis(self, input[0])
        expect1 = ["((()))","(()())","(())()","()(())","()()()"]

        out2 = Solution.generateparenthesis(self,input[1])
        expect2 = ["()"]

        for i in range(len(out1)):
            self.assertIn(out1[i],expect1)

        self.assertEqual(len(out1),len(expect1))

        for i in range(len(out2)):
            self.assertIn(out2[i],expect2)

        self.assertEqual(len(out2),len(expect2))

if __name__ == '__main__':
    unittest.main()

