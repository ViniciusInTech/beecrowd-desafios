numeros_positivos = 0
media_numeros_positivos = 0

for _ in range(6):
    numero = float(input())
    if numero > 0:
        numeros_positivos +=1
        media_numeros_positivos += numero

media_numeros_positivos = media_numeros_positivos/numeros_positivos
print(f"{numeros_positivos} valores positivos")
print(f"{media_numeros_positivos:.1f}")