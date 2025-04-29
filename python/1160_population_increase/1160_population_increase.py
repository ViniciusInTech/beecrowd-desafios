def population_growth(T, test_cases):
    results = []
    for i in range(T):
        PA, PB, G1, G2 = test_cases[i]
        years = 0

        while PA <= PB and years <= 100:
            PA += int(PA * (G1 / 100))
            PB += int(PB * (G2 / 100))
            years += 1

        if years > 100:
            results.append("Mais de 1 seculo.")
        else:
            results.append(f"{years} anos.")

    return results

n = int(input())
test_cases = []
for _ in range(n):
    dados_cidade = map(float, input().split())
    test_cases.append(dados_cidade)
results = population_growth(n, test_cases)
for result in results:
    print(result)
