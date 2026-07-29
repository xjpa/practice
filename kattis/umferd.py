# https://open.kattis.com/problems/umferd

m = int(input())
n = int(input())

empty_count = 0

for _ in range(n):
    lane = input()
    empty_count += lane.count(".")

total_cells = m * n

print(empty_count / total_cells)