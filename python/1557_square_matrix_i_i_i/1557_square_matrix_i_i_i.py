while True:
    n = int(input())
    if n == 0:
        break

    max_num = 2 ** (2 * (n - 1))
    qtde_caracteres = len(str(max_num))

    output = ""
    for y in range(n):
        linha = ""
        for x in range(n):
            num = 2 ** (x + y)
            caracteres = qtde_caracteres - len(str(num))
            linha += f"{' ' * caracteres}{num} "
        output += linha.rstrip()
        if y < n - 1:
            output += "\n"

    print(output)
    print("")
