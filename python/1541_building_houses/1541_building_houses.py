import math


def calculate_land_size(A, B, C):
    house_area = A * B
    max_percentage = C / 100.0
    total_land_area = house_area / max_percentage
    side_length = math.sqrt(total_land_area)
    return int(side_length)


def main():
    while True:
        inputs = input()
        if inputs == '0':
            break
        A, B, C = map(int, inputs.strip().split())
        if A == 0 and B == 0 and C == 0:
            break

        print(calculate_land_size(A, B, C))


if __name__ == "__main__":
    main()
