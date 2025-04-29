def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    sheep = list(map(int, data[1:1 + N]))

    star = [0] * N
    sum_trak = 0
    sum_sheep = 0
    i = 0

    while True:
        if i == 0 and sheep[i] % 2 == 0:
            star[i] = 1
            if sheep[i] > 0:
                sheep[i] -= 1
            break
        elif i == N - 1 and sheep[i] % 2 == 1:
            star[i] = 1
            if sheep[i] > 0:
                sheep[i] -= 1
            break
        elif sheep[i] % 2 == 1:
            sheep[i] -= 1
            star[i] = 1
            i += 1
        elif sheep[i] % 2 == 0:
            star[i] = 1
            if sheep[i] > 0:
                sheep[i] -= 1
            i -= 1

    for i in range(N):
        sum_sheep += sheep[i]
        sum_trak += star[i]

    print(f"{sum_trak} {sum_sheep}")


if __name__ == "__main__":
    main()
