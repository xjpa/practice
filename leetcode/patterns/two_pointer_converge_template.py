"""
two-pointer converge

TEMPLATE:

left starts at beginnig
right starts at end
both move to center
"""

nums = [1,2,3,4,5]

left = 0
right = len(nums - 1)

while left <= right:
    if condition:
        left += 1
    else:
        right -= 1

"""
this is useful for when the needed information is at the edge of a sorted array/string
"""