# https://open.kattis.com/problems/pobudget

revenue_expenses = int(input())
budget = 0

for _ in range(revenue_expenses):
    description = input()
    revenue = int(input())
    budget += revenue

if budget == 0:
    print("Lagom")
elif budget > 0:
    print("Usch, vinst")
else:
    print("Nekad")

# a more pythonic version would probably just use 
# input()
# instead of 
# description = input()
# since the description variable isnt used