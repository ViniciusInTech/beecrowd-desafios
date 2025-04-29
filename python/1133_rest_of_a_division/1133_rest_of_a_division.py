x = int(input())
y = int(input())

x, y = min(x, y), max(x, y)
x += 1
while x < y:
    resto = x % 5
    if 2 == resto or 3 == resto:
        print(x)
    x +=1