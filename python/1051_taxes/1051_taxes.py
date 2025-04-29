salario = float(input())
valor = 0

if salario <= 2000:
    print("Isento")
else:
    taxa_a = min(salario - 2000, 1000) if salario > 2000 else 0
    taxa_b = min(salario - 3000, 1500) if salario > 3000 else 0
    taxa_c = salario - 4500 if salario > 4500 else 0

    valor += (taxa_a * 8) / 100
    valor += (taxa_b * 18) / 100
    valor += (taxa_c * 28) / 100

    print(f"R$ {valor:.2f}")
