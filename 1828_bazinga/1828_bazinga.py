n = int(input())

for i in range(n):
    i += 1
    player, player2 = input().split()
    if player == player2:
        print(f"Caso #{i}: De novo!")
    elif player == "tesoura" and player2 == "papel":
        print(f"Caso #{i}: Bazinga!")
    elif player == "papel" and player2 == "pedra":
        print(f"Caso #{i}: Bazinga!")
    elif player == "pedra" and player2 == "lagarto":
        print(f"Caso #{i}: Bazinga!")
    elif player == "lagarto" and player2 == "Spock":
        print(f"Caso #{i}: Bazinga!")
    elif player == "Spock" and player2 == "tesoura":
        print(f"Caso #{i}: Bazinga!")
    elif player == "tesoura" and player2 == "lagarto":
        print(f"Caso #{i}: Bazinga!")
    elif player == "lagarto" and player2 == "papel":
        print(f"Caso #{i}: Bazinga!")
    elif player == "papel" and player2 == "Spock":
        print(f"Caso #{i}: Bazinga!")
    elif player == "Spock" and player2 == "pedra":
        print(f"Caso #{i}: Bazinga!")
    elif player == "pedra" and player2 == "tesoura":
        print(f"Caso #{i}: Bazinga!")
    else:
        print(f"Caso #{i}: Raj trapaceou!")
