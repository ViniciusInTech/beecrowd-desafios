i = int(input())

for _ in range(i):
    n = int(input())
    number = 1
    sequencia = [0]
    for s in range(n):
        novo_number = sequencia[-1] + number
        sequencia.append(number)
        number = novo_number
    print(f"Fib({n}) = {sequencia[-1]}")