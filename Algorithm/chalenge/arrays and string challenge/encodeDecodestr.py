'''
Design an algorithm to encode a list of strings to a string

'''

class Solution:
    def encode(self,strs):
        '''
        @param: strs: a list of strings
        @return: encodes a lists of strings in to a strings
        '''

        res = ''
        for s in strs:
            res += str(len(s)) + ";" + s
        return res

    def decode(self,str):
        '''
        @param: str: astring
        @return: decodes a single str to a list of strings
        '''

        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != ";":
                j+=1

            length = int(str[i:j])

            res.append(str[j +1 : j+1 + length])
            i = j + 1 + length

        return res


