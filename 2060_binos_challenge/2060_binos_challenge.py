# Step 1: Read the input
N = int(input())
numbers = list(map(int, input().split()))

multiples_of_2 = 0
multiples_of_3 = 0
multiples_of_4 = 0
multiples_of_5 = 0

for number in numbers:
    if number % 2 == 0:
        multiples_of_2 += 1
    if number % 3 == 0:
        multiples_of_3 += 1
    if number % 4 == 0:
        multiples_of_4 += 1
    if number % 5 == 0:
        multiples_of_5 += 1

print(f"{multiples_of_2} Multiplo(s) de 2")
print(f"{multiples_of_3} Multiplo(s) de 3")
print(f"{multiples_of_4} Multiplo(s) de 4")
print(f"{multiples_of_5} Multiplo(s) de 5")
