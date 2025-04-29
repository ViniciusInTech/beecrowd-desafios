x, y = map(int, input().split())

n = 1
while n <= y:
    output = ""
    for z in range(x):
        if n <= y:
            output += f"{n} "
            n += 1
    print(output.strip())
