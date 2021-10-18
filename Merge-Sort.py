"""
Divide and conquer is an algorithmic paradigm that breaks a problem into subproblems and recursively solves the subproblems 
and then finally combines the solutions to the subproblems to solve the original problem. Since they're solved recursively,
each subproblem must be smaller than the original problem and there must be a base case for subproblems.

Merge sort employ divide and conquer based on recursion with running time of O(nlogn).
It works likes this:
1) Divide: find the midpoint of the array
2) Conquer: sort the subarrays created in the divide step. Recursively sort the subarrays (call mergesort twice on the two subarrays),
if it has more than 2 elements and it's no the base case, then it is divided into subarrays again until base case of size 1.
3) Combine: merge the 2 sorted subarrays back into a single sorted subarray.
"""
