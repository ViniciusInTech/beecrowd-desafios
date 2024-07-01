import sys
input = sys.stdin.read
data = input().split()

C = int(data[0])

T = data[1]

M = []
index = 2
for i in range(12):
    row = []
    for j in range(12):
        row.append(float(data[index]))
        index += 1
    M.append(row)

column_elements = [M[i][C] for i in range(12)]

if T == 'S':
    result = sum(column_elements)
elif T == 'M':
    result = sum(column_elements) / 12

print(f"{result:.1f}")
