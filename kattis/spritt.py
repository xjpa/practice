# https://open.kattis.com/problems/spritt

n, m = map(int, input().split())
sum = 0
for i in range(n):
    add = int(input())
    sum += add

# i often mess up boundary-inclusive conditions
# such as for this i initially submitted 
# using "<" instead of "<=" because of habit
if sum <= m:
    print("Jebb")
else:
    print("Neibb")