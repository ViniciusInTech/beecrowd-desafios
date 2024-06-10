x = int(input())
y = int(input())

x, y = min(x, y), max(x, y)

sum = 0
while x <= y:
    if x % 13 != 0:
        sum += x
    x += 1

print(sum)