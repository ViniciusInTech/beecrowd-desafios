def determine_winner(player1, player2):
    if player1 == "ataque" and player2 == "ataque":
        return "Aniquilacao mutua"
    elif player1 == "ataque" and player2 in ["pedra", "papel"]:
        return "Jogador 1 venceu"
    elif player1 == "pedra" and player2 == "ataque":
        return "Jogador 2 venceu"
    elif player1 == "pedra" and player2 == "pedra":
        return "Sem ganhador"
    elif player1 == "pedra" and player2 == "papel":
        return "Jogador 1 venceu"
    elif player1 == "papel" and player2 == "ataque":
        return "Jogador 2 venceu"
    elif player1 == "papel" and player2 == "pedra":
        return "Jogador 2 venceu"
    elif player1 == "papel" and player2 == "papel":
        return "Ambos venceram"
    else:
        return "Sem ganhador"


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])
    results = []
    index = 1
    for _ in range(N):
        player1 = data[index]
        player2 = data[index + 1]
        result = determine_winner(player1, player2)
        results.append(result)
        index += 2

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
