tabela_de_precos ={
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

codigo, qtde = map(int, input().split(" "))

print(f"Total: R$ {tabela_de_precos[codigo]*qtde:.2f}")