n = int(input())

valores = {}
for _ in range(n):
    a, b = map(float, input().split())
    valores[int(a)] = b

maior_nota_chave = max(valores, key=valores.get)
maior_valor = valores[maior_nota_chave]

if maior_valor < 8:
    print("Minimum note not reached")
else:
    print(maior_nota_chave)


