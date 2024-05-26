valor = float(input())

valor_centavos = int(round(valor * 100))

cedulas = {
    10000: 0,
    5000: 0,
    2000: 0,
    1000: 0,
    500: 0,
    200: 0
}

moedas = {
    100: 0,
    50: 0,
    25: 0,
    10: 0,
    5: 0,
    1: 0
}

print("NOTAS:")
for cedula in cedulas:
    qtde = valor_centavos // cedula
    valor_centavos -= qtde * cedula
    cedulas[cedula] = qtde
    print(f"{qtde} nota(s) de R$ {cedula / 100:.2f}")

print("MOEDAS:")
for moeda in moedas:
    qtde = valor_centavos // moeda
    valor_centavos -= qtde * moeda
    moedas[moeda] = qtde
    print(f"{qtde} moeda(s) de R$ {moeda / 100:.2f}")
