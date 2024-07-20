def binary_to_decimal(binary_str):
    return int(binary_str, 2)


def process_input(lines):
    results = []
    current_sum = 0

    for line in lines:
        line = line.strip()
        if line == "caw caw":
            results.append(current_sum)
            current_sum = 0
        else:
            binary_str = line.replace('*', '1').replace('-', '0')
            current_sum += binary_to_decimal(binary_str)

    if current_sum > 0 or len(results) == 0:
        results.append(current_sum)

    return results


def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    results = process_input(input_lines)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
