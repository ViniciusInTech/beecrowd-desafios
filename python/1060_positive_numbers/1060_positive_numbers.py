numero_positivo = 0

for _ in range(6):
    numero = float(input())
    if numero > 0:
        numero_positivo += 1

print(f"{numero_positivo} valores positivos")