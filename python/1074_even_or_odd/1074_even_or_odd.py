n = int(input())

for _ in range(n):
    numero = int(input())
    if numero == 0:
        print("NULL")
    elif numero > 0:
        print("ODD POSITIVE" if numero % 2 != 0 else "EVEN POSITIVE")
    elif numero < 0:
        print("ODD NEGATIVE" if numero % 2 != 0 else "EVEN NEGATIVE")