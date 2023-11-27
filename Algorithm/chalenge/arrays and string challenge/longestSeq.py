'''
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
'''
import unittest
from unittest import TestCase

class Solution:
    def naiveSolution(self, nums: [int]) -> int:
        longest = 0

        # utilise set() to eliminate duplicates

        nums_int = set(nums)

        for n in nums_int:
            if (n-1) not in nums_int:
                length = 1
                while (n+length) in nums_int:
                    length +=1
                longest = max(longest, length)


        return longest



class TestSequence(TestCase):
    def setUp(self):
        self.input1 = [0,3,7,2,5,8,4,6,0,1]
        self.input2 = [100,4,200,1,3,2]

    def test_output_number(self):
        output1 = Solution.naiveSolution(self,self.input1)
        output2 = Solution.naiveSolution(self,self.input2)

        self.assertEqual(9, output1)
        self.assertEqual(4, output2)

if __name__ == '__main__':
    unittest.main()