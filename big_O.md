# BigO
The purpose of big O notation is to identify efficiency of an algorithm

It is defined as O(<complexity>)
+ complexity means time complexity and space complexity

We are going to consider the worst case scenario.

We are going to assuming that the hardware and the software that we are going to apply the algorithm is capable.

# O(1):
+ Time complexity is usually what we have to improve to lower the latencies
This is simply means the current operation does not depend on input size.
Time does not impacted by the input size, which is the best.

# O(n):
The time that are taken to compute grows linearly with the size of the input
an example is that we are going to open presents from Santa Clause. Provided that all the present looks the same on the outside.
Which means that if we have millions of presents, we have to open each of them to know what in each present.

# O(logn):
With every step, we are going to eliminate half of the number of given input size.
A practical example: an address look up. We take the input required address, we eliminate each part, From Country-City-street-postcode-house-number. 

# O(nlogn):
Once the input has been integrated through once, each step we are going to eliminate 50% of the given input size.
An example is a card game, Where we got a hand of 13 cards, we have to look through each and every card to determine their values and then start to shuffle them.

# O(n^2) and O(n^3) and O(2^n) and  O(n!):
+ n-squared means we have work work with all the elements for each elements.(quadratic time complexity)
+ n-cubed means we have to do the quadratic time complexity and then have to check them one more time.
O(2^n) and O(n!) is the time complexity to of exponentials values.
