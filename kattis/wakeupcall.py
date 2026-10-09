# https://open.kattis.com/problems/wakeupcall

n, m = map(int, input().split())
button_1 = sum(map(int, input().split()))
button_2 = sum(map(int, input().split()))

if button_1 > button_2:
    print("Button 1")
elif button_2 > button_1:
    print("Button 2")
else:
    print("Oh no")