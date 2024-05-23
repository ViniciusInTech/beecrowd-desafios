a, b, c = map(int, input().split(" "))


def maior_ab(a, b):
    return (a + b +abs(a-b))/2


maior = maior_ab(a, b)
maior = maior_ab(maior, c)

print(f"{maior:.0f} eh o maior")
