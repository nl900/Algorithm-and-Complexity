"""


Consider the problem of calculating the factorial n! where
n!=n*(n-1)!

Below is the iterative solution.
Time complexity is the number of cycles repeated inside the loop O(n)
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
 

 Time complexity is the number of times it is called. O(n)
 
 Recursion consumes more space and can lead to huge recursive stacks.
 For every recursive call, a stack is used.
 Space complexity for recursion 
 
 """
def recurs_factorial(n):
    if n == 0:
        return 1;
    return n * recurs_factorial(n-1)
  
