numeros_par = 0
numeros_impar = 0
numeros_positivos = 0
numeros_negativo = 0

for _ in range(5):
    numero = int(input())
    numeros_par += 1 if numero % 2 == 0 else 0
    numeros_impar += 1 if numero % 2 != 0 else 0
    numeros_positivos += 1 if numero > 0 else 0
    numeros_negativo += 1 if numero < 0 else 0

print(f"{numeros_par} valor(es) par(es)")
print(f"{numeros_impar} valor(es) impar(es)")
print(f"{numeros_positivos} valor(es) positivo(s)")
print(f"{numeros_negativo} valor(es) negativo(s)")