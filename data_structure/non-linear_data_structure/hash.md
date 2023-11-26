# Non-linear Data Structure: hash Map
Properties: key, Value, like a dictionary.

We are storing key and value. The key is made usually by a hashfunction.
A hash map means we are storing the value as key through computaional method of a hash function.

example:
a list of 5 element
```python
ki = [12,11,13,14,15]

# hasmap function to store the element value above.
def hashfunction(v):
    # our computation
    return k

# we update our hashmap with our key-value pair
for v in ki:
    k = hasfunction(v)
    hashmap.update({k:v})

```

In case that we want to check if our hashmap has an existing value or not, we simply:
1. Pass the value through the `hashfunction` to get the key
2. look up the key and check if the key hold the same value or not.

The adventage of the hash map is that, after we has stored the value, to search if the value is present or not,
the complexity is O(1)

## Update value of the hashmap

There is a concept of collision happened when we want to store the new value,
we could implement a new data type to store our value, typically a linked list.

## Hasfunction:
An effective hash function will help to distrubuted the value evenly, python has a built in `hash()`

Hash map is dynamic in nature,
Add a varable : O(1)
A key cannot be a Null value
Delete variable also O(1)
Searching also O(1)
sort? because there is no inherite function for that, so we consider this opration as O(nlogn)

## Disadvantage:
+ No duplicate keys
+ Duplicate value is stored in the same key


# Hashset:
Is value-only hashmap.
hashset also not allowed for duplicate value.

==Hash==
Check duplicate and return the duplicate value.
we create a hashset, if the element is not in hash set, we add the element
if an element is present in the hash set, we return the value.

What if we want to return the index value:
in HashMap, we create a K-V pair to store both the value and the index.
when the value is present in the key, we return the duplicate entry, we have already done this in Two Sum
==.==




