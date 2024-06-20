i = int(input())

for _ in range(i):
    n = int(input())
    divisores = 0
    for x in range(n):
        x += 1
        if n % x == 0:
            divisores += 1

    if divisores > 2:
        print(f"{n} nao eh primo")
    else:
        print(f"{n} eh primo")
