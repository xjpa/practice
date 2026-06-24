# https://open.kattis.com/problems/bladra2

velocity,acceleration,time = map(int, input().split())

print((velocity * time) + (0.5 * (acceleration * time **2)))