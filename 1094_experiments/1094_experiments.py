n = int(input())
coelho = 0
rato = 0
sapo = 0

for _ in range(n):
    quantidade, especie = input().split(" ")
    quantidade = int(quantidade)

    coelho += quantidade if especie == "C" else 0
    rato += quantidade if especie == "R" else 0
    sapo += quantidade if especie == "S" else 0

total = coelho+rato+sapo
p_coelho = (coelho / total) * 100
p_rato = (rato / total) * 100
p_sapo = (sapo / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {p_coelho:.2f} %")
print(f"Percentual de ratos: {p_rato:.2f} %")
print(f"Percentual de sapos: {p_sapo:.2f} %")

