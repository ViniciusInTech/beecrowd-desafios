def can_form_triangle(a, b, c, d):
    rods = [a, b, c, d]

    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                x, y, z = rods[i], rods[j], rods[k]
                x, y, z = sorted([x, y, z])
                if x + y > z:
                    return 'S'
    return 'N'


a, b, c, d = map(int, input().split())

print(can_form_triangle(a, b, c, d))
