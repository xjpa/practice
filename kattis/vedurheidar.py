# https://open.kattis.com/problems/vedurheidar

current_speed = int(input())
number_roads = int(input())

for _ in range(number_roads):
    road, max_speed = input().split()
    max_speed = int(max_speed)

    if current_speed > max_speed:
        print(road, "lokud")
    else:
        print(road, "opin")