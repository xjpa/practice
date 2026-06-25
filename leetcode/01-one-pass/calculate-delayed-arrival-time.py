# https://leetcode.com/problems/calculate-delayed-arrival-time/

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        time = arrivalTime + delayedTime
        if time >= 24:
            time = time % 24
        return time
            

# perhaps more cleaner is  just a one liner like:

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24

