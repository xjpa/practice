# https://open.kattis.com/problems/aldur

n = int(input())

youngest = 10**9 # start with largets number so we can rset it immediately to wjhatever is lowest

for i in range (n):
    a = int(input())
    if a < youngest:
        youngest = a

print(youngest)
