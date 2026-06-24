# i think for the following i can do 2 loops, 
# where we compare the current to others in the loop. 
#
# then another approach is store everytihng 
# in a hash table/set, 
# first comparing if weve included it already 
# and if we havent seen it then store

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
    
# time 
# O(n)
# as we only scan array once

# space
# O(n)
# as in worst case we store all cos everything
# would be unique in worse case