def print_pattern(N):
    for i in range(1, N + 1):
        print(f"{i} {i * i} {i * i * i}")
        print(f"{i} {i * i + 1} {i * i * i + 1}")

N = int(input().strip())

print_pattern(N)
