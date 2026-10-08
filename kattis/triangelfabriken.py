# https://open.kattis.com/problems/triangelfabriken

a,b,c=(int(input()) for _ in range(3))

# alternatively i could get the largrst in 1 liner:
# largest=max(a,b,c)

# but i think this is a good exercise to just manually write the comparisons:

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

if largest > 90:
    print("Trubbig Triangel")
elif largest == 90:
    print("Ratvinklig Triangel")
else:
    print("Spetsig Triangel")