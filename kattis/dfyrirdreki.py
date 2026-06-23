# https://open.kattis.com/problems/dfyrirdreki
# polynomial problem
a = int(input())
b = int(input())
c = int(input())

# used discriminant formula
# from https://en.wikipedia.org/wiki/Quadratic_formula
d = b * b - 4 * a * c

if d > 0:
    print(2)
elif d == 0:
    print(1)
else:
    print(0)