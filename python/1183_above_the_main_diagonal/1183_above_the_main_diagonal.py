operation = input().strip()
matrix = []

for i in range(12):
    row = []
    for j in range(12):
        value = float(input().strip())
        row.append(value)
    matrix.append(row)

sum_above_diagonal = 0
count = 0

for i in range(12):
    for j in range(i + 1, 12):
        sum_above_diagonal += matrix[i][j]
        count += 1

if operation == 'S':
    result = sum_above_diagonal
elif operation == 'M':
    result = sum_above_diagonal / count

print(f"{result:.1f}")
