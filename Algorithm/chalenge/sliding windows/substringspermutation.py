'''
check if a string include a permutation of a substring
'''

import unittest

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # method for hash management:
        def create_hash(s:str):
            map = {}
            for character in s:
                position = ord(character)-ord('a')
                val = map.get(position,0)
                map[position] = 1 + val
            return map
        def insert_item(character,map:{}):
            position = ord(character)-ord('a')
            map[position] = 1 + map.get(position, 0)
            return map
        def pop_value(character, map:{}):
            position = ord(character)-ord('a')
            map[position] = map.get(position, 0) -1
            if map[position] <=0:
                map.pop(position)
            return map

        # create hash for s1:
        s1_map = create_hash(s1)
        # window sliders
        l, r = 0, len(s1)-1
        # create a hash of the window if hash is none
        win_hash = create_hash(s2[l:r+1])
        res = False
        # loop through the s2
        while r < len(s2) and res == False:
            # compare the hash value
            if win_hash.items() != s1_map.items():
                r +=1
                # insert new character to hash if we are in bound
                if r < len(s2):
                    insert_item(s2[r],win_hash)

                # pop values from r when we move our window
                pop_value(s2[l],win_hash)
                l +=1
            else:
                res = True

        return res


class Yourtest(unittest.TestCase):
    def test_inclusion(self):
        s1 = "ab"
        s2 = "eidbaooo"
        s3 = "eidboaoo"
        self.assertTrue(Solution.checkInclusion(self,s1,s2))
        self.assertFalse(Solution.checkInclusion(self,s1,s3))

if __name__ == '__main__':
    unittest.main()

