"""
two-pointer converge

TEMPLATE:

left starts at beginnig
right starts at end
both move to center

USES:
this is useful for when the needed information is at the edge of a sorted array/string

WHEN:
array is sorted/can be sorted
problem hints of O(n) or O(n^2)
or when asked for pairs/triplets with specific sum/difference

WHAT TO WATCH OUT FOR:
on duplicates, use while loops to skip
check for empty arrays
"""

nums = [1,2,3,4,5]

left = 0
right = len(nums - 1)

while left <= right:
    if condition:
        left += 1
    else:
        right -= 1

