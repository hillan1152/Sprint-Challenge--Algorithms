#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) -- the size of n determines the size of the loop


b) O(n^2) -- for loop with a nested loop based on the size of n


c) O(n) -- runs based on the size of bunnies

## Exercise II
n
n
n
n
n  f(can be anywhere)
n
n

f = ?

Since the goal is to minimize the amount of broken eggs, I would start from the lowest floor "f" and drop an egg. If the egg doesn't break (False), continue to the next floor and forgo the process until the first egg breaks. If the egg breaks is True, f = n. 

The run time complexity would be O(n) because we are unsure about the number of floors and n will dictate what floor it will land on. 