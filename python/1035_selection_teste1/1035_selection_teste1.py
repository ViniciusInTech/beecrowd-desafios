a, b, c, d = map(int, input().split(" "))


def is_greater(x, y):
    return x > y


def is_positive(x):
    return x > 0


def is_even(x):
    return x % 2 == 0


def values_are_valid(a, b, c, d):
    return (is_greater(b, c) and
            is_greater(d, a) and
            is_greater(c + d, a + b) and
            is_positive(c) and
            is_positive(d) and
            is_even(a))


if values_are_valid(a, b, c, d):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
