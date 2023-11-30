'''
Given an integer array nums of unique elements, return all possible subsets
(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
'''

import unittest

class Solution:
    def subsets(self, nums: [int] )-> [[int]]:
        # base case
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include the nums[i]

            subset.append(nums[i])
            dfs(i+1)

            #decision not to include the nums[i]:
            subset.pop()
            dfs(i +1)

        dfs(0)

        return res

class Yourtest(unittest.TestCase):
    def test_subsets(self):
        input1 = [1,2,3]
        output1 = Solution.subsets(self,input1)
        sol1 =[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        for item in output1:
            self.assertIn(item, sol1)

        input2 = [0]
        output2 = Solution.subsets(self,input2)
        sol2 =[[],[0]]
        for item in output2:
            self.assertIn(item, sol2)

        self.assertEqual(len(output1),len(sol1))
        self.assertEqual(len(output2),len(sol2))


if __name__ == '__main__':
    unittest.main()

