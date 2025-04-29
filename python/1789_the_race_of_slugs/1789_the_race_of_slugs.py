import sys

def get_slug_level(speed):
    if speed < 10:
        return 1
    elif speed < 20:
        return 2
    else:
        return 3

def process_input(input_data):
    lines = input_data.strip().split('\n')
    results = []
    for i in range(0, len(lines), 2):
        L = int(lines[i])
        speeds = list(map(int, lines[i + 1].split()))
        max_speed = max(speeds)
        results.append(get_slug_level(max_speed))
    return results

def main():
    input_data = sys.stdin.read()
    results = process_input(input_data)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
