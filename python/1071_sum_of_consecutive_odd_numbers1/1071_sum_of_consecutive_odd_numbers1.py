x = int(input())
y = int(input())

a, b = min(x, y), max(x, y)

soma = 0

for i in range(a + 1, b):
    if i % 2 != 0:
        soma += i

print(soma)
