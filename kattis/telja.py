# https://open.kattis.com/problems/telja

n = int(input())
i = 0
while i < n:
    i += 1
    print(i)

# i think this is a cleaner version
n = int(input())

for i in range(1, n+1):
    # start at 1, stop before n+1
    print(i)