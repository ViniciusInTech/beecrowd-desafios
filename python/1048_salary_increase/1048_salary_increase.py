salario = float(input())
reajuste = 0

if 0 < salario <= 400:
    reajuste = 15
elif 400.01 < salario <= 800:
    reajuste = 12
elif 800.00 < salario <= 1200:
    reajuste = 10
elif 1200.00 < salario <= 2000:
    reajuste = 7
else:
    reajuste = 4

aumento = (salario * reajuste) / 100
print(f"Novo salario: {salario+aumento:.2f}")
print(f"Reajuste ganho: {aumento:.2f}")
print(f"Em percentual: {reajuste} %")
