N, M = map(int, input().split())

for _ in range(M):
    acao = input().strip()
    if acao == 'fechou':
        N += 1
    elif acao == 'clicou':
        N -= 1

print(N)
