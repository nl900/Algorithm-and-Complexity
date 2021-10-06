"""
Consider the problem of calculating the factorial n! where
n!=n*(n-1)!

Below is the iterative solution.
Time complexity is the number of cycles O(n)
Space complexity O(1)
"""

def iter_factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
  
 """
 Recursion is when a function calls itself. Here is the recursive solution 
 to the factorial problem.
 
 Time complexity is the number of times the function is called. O(n)
 
 Recursion consumes more space as for every recursive call, the state is saved to
 the call stack. This can lead to huge recursive stacks
 For factorial(6) a stack of 6 is required until the call is amde to factorial(0)
 and the value is finally computed. So a stack of size N is implicitly allocated for 
 storing the state of function calls. O(n)
 """
def recurs_factorial(n):
    if n == 0:
        return 1;
    return n * recurs_factorial(n-1)
  
