import unittest

class Solution:
    def search(self, nums: [int], target: int) -> int:
        # have pointers to keep track of index
        #left pointer and right pointer

        Left = 0
        Right = len(nums)-1

        # base case
        while Left <= Right:
            n = (Left+Right) // 2
            if nums[n] > target:
                Right = n -1
            elif nums[n]< target:
                Left = n+1
            else:
                return n

        return -1

class Yourtest(unittest.TestCase):
    def test_yourtest(self):
        input = [-1,0,3,5,9,12]
        target = 9
        output = Solution.search(self,input,target)
        self.assertEqual(output,4)

if __name__ == '__main__':
    unittest.main()

