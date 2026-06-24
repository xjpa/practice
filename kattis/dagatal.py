# https://open.kattis.com/problems/dagatal


# no specific formula needed for this one
# just memorize the number of days and if its leap year
# then february gets a +1
# but the year is already given, 2019, w/c is not a leap year
m = int(input())

month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

print(month_days[m-1])