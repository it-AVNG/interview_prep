# Linear Data Structures

## Arrays
Arrays usually fixed in size.

### properties:
+ size: The number of element there are in the arrays.
+ indexing: to access elements in the arrays.

Common trap: Inteviewer said :"index starting at 1". Sometimes throws people off. But just remember, the index is actually refers back to the 1st element.
In norm, the index starts from '0', the 2nd element is '1' step away from the 1st element, so its index is `1`.
Then if the index starts at "1", the 2nd element will have the index of "2".

*Note*: As long as we have in mind the index, we can calls the value at that index as we wish.
### Method:
+ `set(i)`, `insert(i)` or, `retrieve(i)` : set, retrieve the value at index `i`.
  The operation is of O(1) complexity. No matter how large the input is, we only have 1 operation to set it.

+ `find(v)`: iterate through the arrays index to find the element that is equal to the input value.
  The operation is of O(n) in the unsorted arrays.

*note*: in the sorted Arrays, provided we know the array is sorted, we only need to look at the middle value, comparing our requirements with it.
If our input is not at the middle we look to the left (in case the input is lower than the middle value) and try again.
The reverse is true if the input is larger than the middle value. 
Everytime, we would reduce the size of the interested group by half, in this case the complexity is O(logn)

---

Interview problem:
==Two Sum==
Given an array, find a pair of element which their sum is equal to a number and returns their position.

The approach:
+ Brute Force: iterate through the list, take the input number and compute the difference between the input and the element value.
Find the from the rest of the list, if there is a value equal to computed value, returns the pairs. This is a O(n^2)

+ Layman: Sort the array, then look at the 1st element, compute the difference between the 1st element and the input, use binary search for the rest of the elements
If the value is found, returns the value. The time complexity is O(nlogn)

+ Hashmap: a key value pair structures using dict. Check if the difference is present in the Hash map. If not, add the 'key value' pair.
Where the 'key' is the value of the element and the 'value' is the 'index'

and as we move the entry to the hashmap,we will eventually encounter the pair. 
We only iterate once, so the time complexity is O(n), the space complexity is also the O(n)

---
TODO: create a python file for all of the solution

