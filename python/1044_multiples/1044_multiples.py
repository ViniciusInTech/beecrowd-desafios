a, b = map(int, input().split(" "))


def menor(a, b):
    if a > b:
        return b, a
    return a, b

a, b = menor(a, b)
resto = b // a
if a * resto == b:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
