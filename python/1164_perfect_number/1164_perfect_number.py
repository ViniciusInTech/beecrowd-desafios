i = int(input())

for _ in range(i):
    n = int(input())
    soma_divisores = 0
    for x in range(n-1):
        x += 1
        if n % x == 0:
            soma_divisores += x
    if soma_divisores == n:
        print(f"{n} eh perfeito")
    else:
        print(f"{n} nao eh perfeito")