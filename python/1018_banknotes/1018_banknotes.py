valor = int(input())

cedulas = {
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0
}

print(valor)
for cedula in cedulas:
    quantidade_de_cedulas = valor//cedula
    if quantidade_de_cedulas > 0:
        valor -= cedula*quantidade_de_cedulas
    cedulas[cedula] = quantidade_de_cedulas

    print(f"{quantidade_de_cedulas} nota(s) de R$ {cedula},00")
