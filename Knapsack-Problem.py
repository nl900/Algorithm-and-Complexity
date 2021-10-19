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
  if n==0 or c==0: # base case
    return 0
  # if the weight of the current item is more than c, this item can't be included in the
  # optimal solution 
  if (w[n-1] > c):
    return brute_knapsack(c, w, v, n-1)
  # pick the maximum value subset, the max of 
  # 1) Value of the nth item plus max value obtained by adding n-1 items
  # 2) Max value obtained by adding n-1 items, excluding the nth item
  # and recursively process the remaining items
  else:
    return max(v[n-1] + brute_knapsack(c-w[n-1], w, v, n-1), brute_knapsack(c, w, v, n-1))

"""
Optimal substructure: the optimal solution can be constructed from the optimal solutions
of its subproblems.
The max value is obtained by taking the max of 
* n-1 items
* Value of the nth item plus the max value obtained by adding n-1 items
The max value obtained by adding n-1 items is the optimal solution to a subproblem.
The optimal solution of the problem can be constructed using the optimal solutions of the 
subproblems.
So the knapsack problem has the optimal substructure property.

Analyzing the recursion tree, for c and n (current index), brute_knapsack(1,1) is being
called twice. The overlapping subproblem property.

The two properties makes it an ideal candidate for dynamic programming.
"""
