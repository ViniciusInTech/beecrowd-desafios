alcohol, gasoline, diesel = 0, 0, 0

while True:
    entrada = int(input())
    if entrada == 4:
        break
    elif entrada == 1:
        alcohol += 1
    elif entrada == 2:
        gasoline += 1
    elif entrada == 3:
        diesel += 1


print("MUITO OBRIGADO")
print(f"Alcool: {alcohol}")
print(f"Gasolina: {gasoline}")
print(f"Diesel: {diesel}")