# https://leetcode.com/problems/merge-strings-alternately/
# todo
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i in range(max(len(word1), len(word2))):
            # word 1
            if i < len(word1):
                merged.append(word1[i])
            # alternate to word 2
            if i < len(word2):
                merged.append(word2[i])
            # alternate back to word 1 in next step
            # basically appended 2 arrays to the merged array
        return "".join(merged) 
    # .join() returns a string data type in python

"""
time-spaccocomple:
time = O(n+m) where n and m aer word1 and word2
space = O(n+m) cos we store both shit

my apprpach:

initialize an empty list called merged

get the length of the longer word

loop from i = 0 to longer_length - 1:
    if i is still inside word1:
        append word1[i] to merged

    if i is still inside word2:
        append word2[i] to merged

join merged into a string
return the string
"""

# alternatively

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str: