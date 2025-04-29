n1 = 0
n2 = 0
while True:
    n = float(input())
    if n > 10 or n <= 0:
        print("nota invalida")
    elif n1 == 0:
        n1 += n
    elif n2 == 0:
        n2 += n
        break
media = (n1 + n2) / 2

print(f"media = {media:.2f}")
