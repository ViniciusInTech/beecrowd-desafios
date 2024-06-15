n = int(input())


def soma(a, b):
    return a+b
number = 1
sequencia = [0]
for x in range(n-1):
    novo_number = soma(sequencia[-1], number)
    sequencia.append(number)
    number = novo_number

output = ""
for h in sequencia:
    output += f"{h} "

print(output.strip())

