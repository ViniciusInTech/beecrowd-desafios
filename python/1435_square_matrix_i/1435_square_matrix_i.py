def generate_array(n):
    array = [[1 for _ in range(n)] for _ in range(n)]

    for i in range(1, (n + 1) // 2):
        for j in range(i, n - i):
            for k in range(i, n - i):
                array[j][k] = i + 1

    return array


def print_array(array):
    n = len(array)
    for row in array:
        print(" ".join(f"{num:3d}" for num in row))
    print()


def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        array = generate_array(n)
        print_array(array)


if __name__ == "__main__":
    main()
