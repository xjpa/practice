# need to create a new array that contains all elements of original to add to new array we can append
# then its just a matter of looping

# time: O(n) 
# time complexity is not O(n^2) sicne the outer loop runs a fixed constant 2x or 2n
# nested loops only become O(n^2) when both loops grow with input size
# space: O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):
            for i in nums:
                ans.append(i)
        return ans
    
## alternatively i could just do the following because of python shit

return nums + nums