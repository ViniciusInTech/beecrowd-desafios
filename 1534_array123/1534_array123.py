import sys

input = sys.stdin.read


def main():
    for line in input().splitlines():
        z = int(line.strip())
        ara = [[3] * z for _ in range(z)]

        for a in range(z):
            ara[a][a] = 1

        d = z - 1
        for a in range(z):
            b = d - a
            ara[a][b] = 2

        for row in ara:
            print("".join(map(str, row)))


if __name__ == "__main__":
    main()
