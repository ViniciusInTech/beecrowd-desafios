def can_frog_win(P, pipe_heights):
    N = len(pipe_heights)

    for i in range(N - 1):
        if abs(pipe_heights[i] - pipe_heights[i + 1]) > P:
            return "GAME OVER"

    return "YOU WIN"


P, N = map(int, input().strip().split())
pipe_heights = list(map(int, input().strip().split()))

result = can_frog_win(P, pipe_heights)
print(result)
