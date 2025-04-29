i = int(input())


def simplificar(a, b):
    if a == b:
        return 1, 1
    elif a % 2 == 0 and b % 2 == 0:
        return simplificar(a // 2, b // 2)
    elif a % 3 == 0 and b % 3 == 0:
        return simplificar(a // 3, b // 3)
    elif a % 5 == 0 and b % 5 == 0:
        return simplificar(a // 5, b // 5)
    else:
        return a, b


def sum(n1, n2, d1, d2):
    numerador = (n1*d2) + (n2 * d1)
    denominador = (d1*d2)
    n_simplificado, d_simplificado = simplificar(numerador, denominador)
    print(f"{numerador}/{denominador} = {n_simplificado:.0f}/{d_simplificado:.0f}")


def subtraction(n1, n2, d1, d2):
    numerador = (n1 * d2) - (n2 * d1)
    denominador = (d1 * d2)
    n_simplificado, d_simplificado = simplificar(numerador, denominador)
    print(f"{numerador}/{denominador} = {n_simplificado:.0f}/{d_simplificado:.0f}")


def multiplication(n1, n2, d1, d2):
    numerador = (n1 * n2)
    denominador = (d1 * d2)
    n_simplificado, d_simplificado = simplificar(numerador, denominador)
    print(f"{numerador}/{denominador} = {n_simplificado:.0f}/{d_simplificado:.0f}")


def division(n1, n2, d1, d2):
    numerador = (n1 * d2)
    denominador = (n2 * d1)
    n_simplificado, d_simplificado = simplificar(numerador, denominador)
    print(f"{numerador}/{denominador} = {n_simplificado:.0f}/{d_simplificado:.0f}")

operacoes = {
    "+": sum,
    "-": subtraction,
    "*": multiplication,
    "/": division
}


for _ in range(i):
    n1, b, d1, operador, n2, c, d2 = input().split(" ")

    n1 = int(n1)
    n2 = int(n2)
    d1 = int(d1)
    d2 = int(d2)

    operacao = operacoes[operador](n1, n2, d1, d2)

