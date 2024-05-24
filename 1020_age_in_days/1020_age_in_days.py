days = int(input())

days_conversion = {
    365: 0,
    30: 0,
    1: 0
}

for day in days_conversion:
    quantidade = days//day
    if quantidade > 0:
        days -= quantidade*day
    days_conversion[day] = quantidade

print(f"{days_conversion[365]} ano(s)")
print(f"{days_conversion[30]} mes(es)")
print(f"{days_conversion[1]} dia(s)")

