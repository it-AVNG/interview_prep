'''
Find longest sub string that is not repeating
Using HashSet to keep track of the element existing in the windows
2 pointers left and right, move the right pointer till the point where we don't
encounter any repeating element.
When we encountered a repeated element, we marked that as an end of a sequence
move the left pointer up 1. The left pointer move up and we check if there is duplicate
if yes, move the left once more.
'''

import unittest


class Solution:
    def lengthOfLongestSubstrings(self, string: str) -> int:
        if len(string) == 1 :
            return 1
        elif len(string) == 0:
            return 0
        # create a hash set
        hashset = set()
        # create a pairs of pointer to indices
        left = 0
        right = 0
        # create max variable to hold the output value
        max =0
        count =0
        # loop until the right pointer reaches the end
        while right < len(string):
            # check if the value is not in the set
            if string[right] not in hashset:
                hashset.add(string[right])
                count +=1
            else:
                if count > max:
                    max = count

                # repeat till the right element not in hash set
                while string[right] in hashset:
                # remove the element at the left pointer from the set
                    hashset.discard(string[left])
                    count-=1
                # move the left by 1
                    left +=1

                # add the element
                hashset.add(string[right])
                count +=1

            right +=1

        if count > max:
            max = count

        return max

class TestSlidingWindow(unittest.TestCase):
    def test_substring_max_length(self):
        input = ["abcabcbb","bbbbb","pwwkew","au"]
        output1 = Solution.lengthOfLongestSubstrings(self,input[0])
        output2 = Solution.lengthOfLongestSubstrings(self,input[1])
        output3 = Solution.lengthOfLongestSubstrings(self,input[2])
        output4 = Solution.lengthOfLongestSubstrings(self,input[3])
        self.assertEqual(3, output1)
        self.assertEqual(1, output2)
        self.assertEqual(3, output3)
        self.assertEqual(2, output4)



if __name__ == '__main__':
    unittest.main()