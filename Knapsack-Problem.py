"""
Given weights and values of n items, put these items in a knacpsack with a capacity of C.
Find a subset of items that will maximise total value in the knapsack where the total weight
is not more than C.

The brute-force recursive solution is to try all combinations of items and choose the one with
maximum profit where the weight does not exceed C.
Time complexity exponential O(2^n)
Space complexity O(n) to store the recursive stack
"""

def brute_knapSack():
