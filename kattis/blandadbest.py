# https://open.kattis.com/problems/blandadbest

meat_types = int(input())

if meat_types == 1:
    meat=input()
    if meat == "nautakjot":
        print("nautakjot")
    elif meat == "kjuklingur":
        print("kjuklingur")
else:
    print("blandad best")

# more pythonic, only realised this after submitting my solution lol:

meat_types = int(input())

if meat_types == 1:
    meat = input()
    print(meat)
else:
    print("blandad best")