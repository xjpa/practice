# https://open.kattis.com/problems/goggi

n,q,m=input().split()


# i have to convert to int cos of python edge case of how string comparisons work
# like in python, if string 9 and 100 are strings then "9" > "100" = True so itd return > instead of <
n=int(n)
m=int(m)

if n == m:
    print("Goggi svangur!")
elif n>m:
    print(">")
else:
    print("<")