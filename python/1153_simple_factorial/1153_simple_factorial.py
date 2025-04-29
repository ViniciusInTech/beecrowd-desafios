n = int(input())
x = 1
fatorial = n
while x < n:
    fatorial = fatorial * (n-x)
    x += 1

print(fatorial)