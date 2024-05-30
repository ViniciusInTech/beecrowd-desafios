a, b, c = map(float, input().split(" "))

def forma_triangulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    print("NAO FORMA TRIANGULO")
    return False

def is_triangulo_retangulo(a, b, c):
    if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
        print("TRIANGULO RETANGULO")

def is_triangulo_obtusangulo(a, b, c):
    if (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2) or (c**2 > a**2 + b**2):
        print("TRIANGULO OBTUSANGULO")

def is_triangulo_acutangulo(a, b, c):
    if (a**2 < b**2 + c**2) and (b**2 < a**2 + c**2) and (c**2 < a**2 + b**2):
        print("TRIANGULO ACUTANGULO")

def is_equilatero(a, b, c):
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")

def is_isosceles(a, b, c):
    if (a == b or a == c or b == c) and not (a == b == c):
        print("TRIANGULO ISOSCELES")

if forma_triangulo(a, b, c):
    is_triangulo_retangulo(a, b, c)
    is_triangulo_obtusangulo(a, b, c)
    is_triangulo_acutangulo(a, b, c)
    is_equilatero(a, b, c)
    is_isosceles(a, b, c)
