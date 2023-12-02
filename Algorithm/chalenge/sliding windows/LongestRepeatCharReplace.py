import unittest

'''
create 2 frame l,r and hash map

check if the char at the r frame is in hashmap
    - add to the map if not available in map, value 1
    - increment to the value if available in map
update the windows size

if the windows size - max hashmap values is not larger than k
    - pop the left frame value
    - increase the left frame by 1
    - decrement the size by 1
    - repeat till the windows size and k in in tandem

return the largest result window size
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charmap = {}
        res = 0 # count the total characters

        l = 0

        for r in range(len(s)):
            # update charmap with the value
            val = charmap.get(s[r], 0)
            charmap[s[r]] = 1 + val

            #decrement the window size if it is too much
            while (r-l+1) - max(charmap.values())>k:
                charmap[s[l]] -= 1
                l +=1
            # update the new accepted window size
            # only take the larger size.
            res = max(res,r-l+1)

        return res


class Yourtest(unittest.TestCase):
    def test_K_is_finite(self):
        s = "AABABBA"
        k =1
        out = Solution.characterReplacement(self,s,k)
        self.assertEqual(out,4)
    def test_K_is_zero(self):
        s= "AAAB"
        k =0
        out = Solution.characterReplacement(self,s,k)
        self.assertEqual(out,3)


if __name__ == '__main__':
    unittest.main()

