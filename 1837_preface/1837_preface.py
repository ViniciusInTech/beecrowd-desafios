def euclidean_division(a, b):
    if b == 0:
        raise ValueError("The divisor b cannot be zero")

    q = a // b
    r = a % b

    if r < 0:
        if b > 0:
            r += b
            q -= 1
        else:
            r -= b
            q += 1

    return q, r


a, b = map(int, input().split())
q, r = euclidean_division(a, b)
print(q, r)
