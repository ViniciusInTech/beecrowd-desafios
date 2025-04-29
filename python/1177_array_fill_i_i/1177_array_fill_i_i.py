def fill_vector(T):
    N = [0] * 1000
    for i in range(1000):
        N[i] = i % T
    return N


def main():
    T = int(input())

    if T < 2 or T > 50:
        print("The value of T must be between 2 and 50.")
        return

    N = fill_vector(T)

    for i in range(1000):
        print(f"N[{i}] = {N[i]}")


if __name__ == "__main__":
    main()
