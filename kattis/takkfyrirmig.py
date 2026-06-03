# https://open.kattis.com/problems/takkfyrirmig

i = 0
n = int(input())
while i < n:
    name = input()
    print(f"Takk {name}")
    i+=1

# alternatively

n = int(input())
for _ in range(n):
    name = input()
    print(f"Takk {name}")