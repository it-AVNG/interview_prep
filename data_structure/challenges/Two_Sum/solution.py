"""
Two sum :
assuming we have an array of number
We are looking for a pair of number that sum up to a number int(N)
assuming that each input has exactly 1 solution
create a python function that solve the requirement.
"""


def twoSum(a: list[int], num: int):
    """return a pair of number that has the sum equal to target num"""

    # create an Hashmap
    hashMap = {}
    # iterate through the list
    for v, k in enumerate(a):
        # compute the difference
        res = num - k
        # check the result in the list as a 'key'
        if res in hashMap.keys():
            # if the result is in the list, return the value of the current element and the 'value' found.
            return (v, hashMap.get(res))

        # if the result is not in the list, add the element-index as a 'key-value' pair to dict
        hashMap.update({k: v})
    return "Not Found"


a = [1, 2, 5, 7, 10, 9]
res = twoSum(a, 20)
print(res)

