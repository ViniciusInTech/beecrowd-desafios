n = int(input())
i = 1
while i <= n:
    x, y = map(int, input().split(" "))
    x, y = min(x, y), max(x, y)
    soma = 0
    x += 1
    while x < y:
        soma += x if x % 2 != 0 else 0
        x += 1
    print(soma)
    i += 1

