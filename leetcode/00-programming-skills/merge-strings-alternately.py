# https://leetcode.com/problems/merge-strings-alternately/
# todo
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
        return "".join(merged)

"""
time-spaccocomple:
time = O(n+m) where n and m aer word1 and word2
space = O(n+m) cos we store both shit

my apprpach:

initialize somehing for merged
count the sum length
loop for merging:
    if i is still inside word1
        append the word1[i]
    if i is still insdie word2
        append the word2[i]
return the merged
"""