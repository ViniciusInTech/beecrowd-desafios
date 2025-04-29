def process_matrix():
    import sys
    input = sys.stdin.read

    data = input().split()

    operation = data[0]

    elements = list(map(float, data[1:]))

    M = []
    for i in range(12):
        row = elements[i * 12:(i + 1) * 12]
        M.append(row)

    total_sum = 0
    count = 0
    for i in range(12):
        for j in range(i):
            total_sum += M[i][j]
            count += 1

    if operation == 'S':
        result = total_sum
    elif operation == 'M':
        result = total_sum / count

    print(f"{result:.1f}")


process_matrix()
