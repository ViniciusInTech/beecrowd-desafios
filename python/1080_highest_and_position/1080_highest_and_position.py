
numeros = {}
numeros_posicoes = {}
for i in range(100):
    i += 1
    numero = int(input())
    numeros[numero] = i
    numeros_posicoes[i] = numero

maior_valor = max(numeros)
posicao_maior_valor = numeros_posicoes[maior_valor]

print(maior_valor)
print(posicao_maior_valor)

