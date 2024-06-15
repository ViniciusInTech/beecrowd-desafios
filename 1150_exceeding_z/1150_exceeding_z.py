x = int(input())
z = int(input())
while z <= x:
    z = int(input())

count = 0
sum_val = 0
current = x

while sum_val <= z:
    sum_val += current
    current += 1
    count += 1
print(count)

