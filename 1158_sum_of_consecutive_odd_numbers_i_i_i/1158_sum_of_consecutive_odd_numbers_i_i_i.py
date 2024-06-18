n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    sum_odd_numbers = 0

    if x % 2 == 0:
        x += 1

    for _ in range(y):
        sum_odd_numbers += x
        x += 2

    print(sum_odd_numbers)
