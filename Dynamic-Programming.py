"""
A problem solving technique of breaking the problem into sub problems 
which are solved individually. Dynamic programming optimizes recursive 
programming by storing results of sub problems so there's no need
to recompute the same subproblem again. It trades space efficiency for time efficiency.
Dynamic programming can be applied where subproblem solutions are overlapping
( overlapping subproblems) and having the property of optimal substructure.

Consider the problem of calculating the fibonacci sequence where 
Fib(n) = Fib(n-1) + Fib(n-2)
A sample sequence of 0, 1, 1, 2, 3, 5, 8, 13, 21.....
If you draw out the tree for the recursive solution, you will see there are overlapping
subproblems across branches. eg fb(3) is called to calculate fib(4) and fib(5), and fib(4)
is called to calculate fib(5) also. If we store the results when it was encountered the first 
time, we won't need to recompute it the next time.

Below is a solution to the fibonacci sequence using memoization.
Memoization stores subproblem results in a top down approach where the problem is broken
into smaller and smaller sub problems until the base case is reached. And so the common
solution is recursive. It solves sub problems as they are needed rather than solving all
in order as in bottom-up.
Since memoization store data in a non-sequential way, when it's needed, hashtable is used.

Complexity
In recursive approach, for every value, 2 function calls are made. eg fib(6) calls fib(5)
and fib(4). fib(5) is calling fib(4) and fib(3). O(2^n) exponential complexity.

In dynamic programming approach, we solve each subproblem once with a total of n subproblems.
So O(n)
"""

memoi = {}
def fibonacci(n):
    if n == 0: # base case 1
        return 0
    if n==1: #base case 2
        return 1
    elif n in memoi: #look up rather than recompute
        return memoi[n]
    else: #recursive step
        memoi[n] = fibonacci(n-1) + fibonacci(n-2) #dp!
        return memoi[n]
