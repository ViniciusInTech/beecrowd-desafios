def optimal_third_card(A, B):
    max_card_value = 13

    if A == B:
        return A


    best_card = None
    best_score = -1

    for C in range(1, max_card_value + 1):
        if C == A or C == B:
            score = 1
        else:
            score = 0

        if score > best_score or (score == best_score and C > best_card):
            best_score = score
            best_card = C

    return best_card


import sys

input = sys.stdin.read().strip()
A, B = map(int, input.split())

print(optimal_third_card(A, B))
