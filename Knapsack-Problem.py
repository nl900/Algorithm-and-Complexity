"""
Given weights and values of n items, put these items in a knacpsack with a capacity of C.
Find a subset of items that will maximise total value in the knapsack where the total weight
is not more than C.

The brute-force recursive solution is to try all combinations of items and choose the one with
maximum profit where the weight does not exceed C.
Time complexity exponential O(2^n)
Space complexity O(n) to store the recursive stack
"""

def brute_knapsack(c, w, v, n):
  # base case
  if n==0 or c==0:
    return 0
  # if the weight of the current item is more than c, this item can't be included in the
  # optimal solution 
  if (w[n-1] > c):
    return brute_knapsack(c, w, v, n-1)
  # pick the maximum value subset, the max of 
  # 1) Current item included
  # 2) Current item not included
  # and recursively process the remaining items
  else:
    return max(v[n-1] + brute_knapsack(c-w[n-1], w, v, n-1), brute_knapsack(c, w, v, n-1))

    
