x = int(input())
respostas = input().split(" ")
total_de_acertos = 0

for resposta in respostas:
    if int(resposta) == x:
        total_de_acertos += 1

print(total_de_acertos)
