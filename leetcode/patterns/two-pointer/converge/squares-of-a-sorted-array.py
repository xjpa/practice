# https://leetcode.com/problems/squares-of-a-sorted-array/description/

"""
approach
make an empty list
loop through the input array
append the previously empty list with the squared
return the sorted list

time O(n log n) <-- because sorted()/sorting is nlogn
space O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = []
        for i in nums:
            new.append(i**2)
        # squaring negatives messes up the order so we have to sort
        return sorted(new) 
    
"""
approach 2 without the o(nlogn) is two pointer
"""