# Dynamic Programming:
Dynamic programming is the art of saving the data that we computed.
Then utilise that data, we will use it for other task.

There are 2 approaches to Dynamic programming
## Bottom Up:
Start from the base case and build a solution we want. This is similar to
an iterative approach.

for the bottom up, consider this example:
```python
'''
climbing a staircase, it takes n steps to reach the top
each time either climb 1 or 2 steps
How many distinct way to climb?
'''


```

## Top down:
Start at the end, the result we are looking for, and we break it smaller
till we reach optimal solution. This is ussually implement using recursion

For example the following code:
```python
'''
Compute a sum of 2 factorial number
'''
def factorial:
    ...
    return res

val = factorial(3) + factorial(4)
```

To compute the 3factorial then 4factorial,
we have been computing 3factorial twice. Which is a waste.

We could parse in another parameter to 'save' the value.
Then utilised that value later, which save computation resource.

The process where we add a 'saving' method,
we actually implement dynamic programming.
