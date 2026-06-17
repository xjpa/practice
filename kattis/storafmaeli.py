# https://open.kattis.com/problems/storafmaeli
n = int(input())

if n%10==0:
    print("Jebb")
else:
    print("Neibb")

# this is cleaner, you can have if/else in print()

print("Jebb" if n%10 == 0 else "Neibb")

# we can use in-line if/else for more complex shit like
# print("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F")
# but thatd be spaghetti, best to just stick with simple one