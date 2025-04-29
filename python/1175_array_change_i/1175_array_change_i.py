numbers = []

for i in range(20):
    n = int(input())
    numbers.append(n)

z = 19
while z > -1:
    print(f"N[{19-z}] = {numbers[z]}")
    z -= 1