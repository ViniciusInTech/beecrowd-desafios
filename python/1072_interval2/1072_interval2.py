n_in = 0
n_out = 0
i = int(input())

for _ in range(i):
    n = int(input())
    if 10 <= n <= 20:
        n_in += 1
    else:
        n_out += 1

print(f"{n_in} in")
print(f"{n_out} out")
