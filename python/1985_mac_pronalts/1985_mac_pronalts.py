valores = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

n = int(input())

soma = 0
for _ in range(n):
    id, qtde = map(int, input().split())
    soma += valores[id] * qtde

print(f"{soma:.2f}")
