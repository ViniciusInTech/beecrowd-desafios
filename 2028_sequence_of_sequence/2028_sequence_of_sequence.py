import sys


def generate_sequence(N):
    sequence = []
    for i in range(N + 1):
        sequence.extend([i] * i)
    return sequence


def main():
    case_number = 1
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue

        N = int(line)
        sequence = [0] + generate_sequence(N)  # Add 0 to the beginning of the sequence
        length = len(sequence)

        # Output the result
        if length == 1:
            print(f"Caso {case_number}: 1 numero")
        else:
            print(f"Caso {case_number}: {length} numeros")

        print(" ".join(map(str, sequence)))
        print()  # Blank line after each case

        case_number += 1


if __name__ == "__main__":
    main()
