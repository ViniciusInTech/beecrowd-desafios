import sys

for line in sys.stdin:
    if line.strip() == "":
        continue

    V = float(line.strip())
    D = float(sys.stdin.readline().strip())

    pi = 3.14
    R = D / 2
    A = pi * R * R
    H = V / A

    print(f"ALTURA = {H:.2f}")
    print(f"AREA = {A:.2f}")
