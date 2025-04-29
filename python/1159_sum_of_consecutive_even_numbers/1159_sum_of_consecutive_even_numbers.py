while True:
    n = int(input())
    if n == 0:
        break
    n = n if n % 2 == 0 else n + 1
    sum = 0
    for _ in range(5):
        sum += n
        n += 2
    print(sum)
