while True:
    m, n = map(int, input().split(" "))
    m, n = min(m, n), max(m, n)
    if m == 0 or m < 0:
        break
    soma = 0
    soma_string = ""
    while m <= n:
        soma += m
        soma_string += f"{m} "
        m += 1
    print(f"{soma_string}Sum={soma}")