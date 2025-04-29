def determine_winner(p, j1, j2, r, a):
    if r == 1 and a == 1:
        return "Jogador 2 ganha!"

    if r == 1 and a == 0:
        return "Jogador 1 ganha!"

    if r == 0 and a == 1:
        return "Jogador 1 ganha!"

    sum_j = j1 + j2

    if sum_j % 2 == 0:
        if p == 1:
            return "Jogador 1 ganha!"
        else:
            return "Jogador 2 ganha!"
    else:
        if p == 0:
            return "Jogador 1 ganha!"
        else:
            return "Jogador 2 ganha!"


input_values = input().split()
p, j1, j2, r, a = map(int, input_values)
result = determine_winner(p, j1, j2, r, a)
print(result)
