L = int(input())
T = input()
matrix = []

for i in range(12):
    row = []
    for j in range(12):
        row.append(float(input()))
    matrix.append(row)

selected_line = matrix[L]

if T == 'S':
    result = sum(selected_line)
elif T == 'M':
    result = sum(selected_line) / 12

print(f"{result:.1f}")
