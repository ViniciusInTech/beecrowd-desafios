def calculate_sum_from_a(texto):
    input_values = list(map(int, texto.split()))
    A = input_values[0]
    index = 1

    while True:
        N = input_values[index]
        if N > 0:
            break
        index += 1

    total_sum = sum(A + i for i in range(N))
    print(total_sum)

calculate_sum_from_a(input())
