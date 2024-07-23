n = int(input())

for _ in range(n):
    player, opcao, player_2, opcao_2 = input().split()
    numero, numero_2 = map(int, input().split())
    soma = numero + numero_2
    if soma % 2 == 0:
        print(player if opcao == "PAR" else player_2)
    else:
        print(player_2 if opcao == "PAR" else player)
