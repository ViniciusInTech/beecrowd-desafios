a = 0.0
M = []

T = input().strip()

for _ in range(12):
    row = [float(input()) for _ in range(12)]
    M.append(row)

p = 11
r = 7

for z in range(1, 11):
    if z <= 5:
        for C in range(p, 12):
            a += M[z][C]
        p -= 1
    elif z >= 6:
        for C in range(r, 12):
            a += M[z][C]
        r += 1

if T == 'S':
    print(f"{a:.1f}")
elif T == 'M':
    a /= 30.0
    print(f"{a:.1f}")
