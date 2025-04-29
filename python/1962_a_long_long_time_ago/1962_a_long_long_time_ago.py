n = int(input())

for _ in range(n):
    x = int(input())
    if x < 2015:
        print(f"{2015-x} D.C.")
    else:
        print(f"{x-2014} A.C.")