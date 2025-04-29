numbers = []

for i in range(100):
    n = float(input())
    numbers.append(n)

for i in range(len(numbers)):
    if numbers[i] <= 10:
        print(f"A[{i}] = {numbers[i]}")
