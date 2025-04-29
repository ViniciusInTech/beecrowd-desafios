import sys


def find_subsequence(n1, n2):
    n1 = str(n1)
    n2 = str(n2)
    count = 0
    last_pos = -1

    start = 0
    while True:
        pos = n2.find(n1, start)
        if pos == -1:
            break
        count += 1
        last_pos = pos
        start = pos + 1

    return count, last_pos + 1


def main():
    case_number = 1
    input_data = sys.stdin.read().strip().splitlines()

    for i in range(0, len(input_data), 2):
        n1 = input_data[i]
        n2 = input_data[i + 1]
        count, pos = find_subsequence(n1, n2)

        print(f"Caso #{case_number}:")
        if count > 0:
            print(f"Qtd.Subsequencias: {count}")
            print(f"Pos: {pos}")
        else:
            print("Nao existe subsequencia")
        print()

        case_number += 1


if __name__ == "__main__":
    main()
