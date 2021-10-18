"""
Divide and conquer is an algorithmic paradigm that breaks a problem into subproblems and recursively solves the subproblems 
and then finally combines the solutions to the subproblems to solve the original problem. Since they're solved recursively,
each subproblem must be smaller than the original problem and there must be a base case for subproblems.

Merge sort employ divide and conquer based on recursion.
It works likes this:
1) Divide: find the midpoint of the array and divide into halves
2) Conquer: if it's only 1 element, then it's already sorted, return. Otherwise, call mergesort on the two subarrays.
3) Combine: merge the smaller lists in sorted order.

Running time O(nlogn) as it divides the array in two halves and takes linear time to merge two halves.
Space O(n) for the temporary array
"""

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 # Find midpoint
  
        # Divide into 2 halves
        L = arr[:mid]
        R = arr[mid:]
 
        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half
  
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
