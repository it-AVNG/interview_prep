
# Linear - Data Structure :Linked List

A Linked list is not a list. It is made of nodes that has the memory address
of the node next to it.
It is a linear data structure but it is dynamic in nature.

## Single link list

For single link list, to go to an element, we have to sequentially
traverse the list.
from the 1st element.

## Doubly Link List

Each of the node, hold the information of the previous node and the node
that is next in the list.
Which means, a doubly link list has the method to traverse up and down the list.

## Circular link list

The cycle is continuous, is a doubly link list where the last and the first
node pointing to each other.

Check [link-list construct](../linked-list/construct.py) for basic method of linkedlist.

## Additional method
1. Add top: create a node and point the node to the head, then move the linklist head pointer to the node.
2. delete element: move the node of the previous node to the node after.
3. find: traverse all the node until we reach the element we are looking for.
4. adjust: same as find and then we have additional update method.

---
=Find middle=
given a singly link list, what is the middle of linked list
Brute force: traverse the linked list to find the size and compute the half then traverse again
Rabbit and Hare: have 2 pointer, the 'rabbit' pointer will move twice as fast, when the fast pointer reached the end of the linked list
the slow pointer will be at the middle of the linked list
---
