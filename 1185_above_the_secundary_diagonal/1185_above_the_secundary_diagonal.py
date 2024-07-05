def perform_operation():
    import sys
    input = sys.stdin.read

    data = input().split()

    operation = data[0]

    matrix_elements = list(map(float, data[1:]))

    matrix = []
    for i in range(12):
        row = matrix_elements[i * 12:(i + 1) * 12]
        matrix.append(row)

    total_sum = 0.0
    count = 0

    for i in range(12):
        for j in range(12):
            if i + j < 11:
                total_sum += matrix[i][j]
                count += 1

    if operation == 'S':
        result = total_sum
    elif operation == 'M':
        result = total_sum / count

    print(f"{result:.1f}")


perform_operation()
