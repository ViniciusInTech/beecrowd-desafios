soma = 0
divisor = 0

while True:
    n = int(input())

    if n <= 0:
        break
    soma += n
    divisor += 1

media = soma / divisor
print(f"{media:.2f}")
