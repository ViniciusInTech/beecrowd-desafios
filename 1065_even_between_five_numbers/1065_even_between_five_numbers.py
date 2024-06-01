valores_pares = 0

for _ in range(5):
    numero = int(input())
    if numero % 2 == 0:
        valores_pares +=1


print(f"{valores_pares} valores pares")