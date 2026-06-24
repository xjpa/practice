# https://open.kattis.com/problems/bestagjofin

n = int(input())

best_name = ""
best_score = -1 # -1 to initilaize value at lowest
for _ in range(n):
    current_name, current_score = input().split()
    current_score = int(current_score)
    if current_score > best_score:
        best_score = current_score
        best_name = current_name

# i intially thought of using KV/dictionary 
# but eventually realize that i dont need to store all of them

print(best_name)