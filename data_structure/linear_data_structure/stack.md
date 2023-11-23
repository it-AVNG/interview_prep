# Linear Data Structure: Stack
A stack is like a stack of plate.
When we add to the stack, we add to the top of the stack.
When we de-stack or remove any element, we also have to de-stack from the top.

This process is called LIFO: Last In first Out principle.

A stack is also the alternative method for recursive solution.
Instead of recursively run method, we can iterate through the
population element via a stack.

## Basic method:
+ `push()`: push an element to the top of the stack
+ `pop()`: or sometime called pop top. pop the top of the Stack
+ `peek()`: look at the top element of the stack

## common process:
+ find, delete, update : O(n) complexity because we have to start from the top

## Use case:

+ check parenthesis that it is open the close correctly:
Iterate through the element, If the top of the element is not the same type, add the element to the stack.
If it is the same type, pop the element.
At the end of the element, if the stack is empty, return 'Ok'

## Construct:

Of course we can construct a stack using Link-List. But, a better implementation in Python is to use a List instead.

# Linear Data Structure: Queue
A queue, is similar to a stack. But when we insert an element, or enqueue, we insert at the top.
When we pop an element, or dequeue, we pop at the end.
When we peek at the queue, we look at the first element that is comming out.
Search an element in the Queue is also an O(n) operation.

A queue operate in FIFO principle: first in First out