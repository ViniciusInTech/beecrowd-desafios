soma = 1
n = 2
i = 2
while i <= 39:
    if i % 2 != 0 and i != 1:
        soma += i / n
        n = n * 2
    i += 1

print(f"{soma:.2f}")

