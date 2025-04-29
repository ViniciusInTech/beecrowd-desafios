code, qtde, value = input().split(" ")
qtde = int(qtde)
value = float(value)

code2, qtde2, value2 = input().split(" ")

qtde2 = int(qtde2)
value2 = float(value2)

total = (qtde*value)+(qtde2*value2)

print(f"VALOR A PAGAR: R$ {total:.2f}")


