# https://open.kattis.com/problems/ofugsnuid

n = int(input())

array_numbers = []
for _ in range(n):
    num = int(input())
    array_numbers.append(num)
for c in reversed(array_numbers):
    print(c)

# i think this can be done with a 1-liner but i am not sure if that is considerd pythonic

print(*reversed([int(input()) for _ in range(int(input()))]), sep="\n")

# the * here is the unpacking operator: https://python-refs.readthedocs.io/en/latest/recipes/unpacking-items-from-iterables.html

# to me this is more concise and readable

n = int(input())
array_numbers2 = [int(input()) for _ in range(n)]

print(*reversed(array_numbers2), sep="\n")

"""
this:

[int(input()) for _ in range(n)] 

is shorter version of:

list_numbers = []

for _ in range(n):
    num = int(input())
    list_numbers.append(num)
"""