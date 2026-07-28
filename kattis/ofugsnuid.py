# https://open.kattis.com/problems/ofugsnuid

n = int(input())

array_numbers = []
for _ in range(n):
    num = int(input())
    array_numbers.append(num)
for c in reversed(array_numbers):
    print(c)