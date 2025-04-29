n = int(input())

numbers = list(map(int, input().split()))

menor = min(numbers)
print(f"Menor valor: {menor}")
print(f"Posicao: {numbers.index(menor)}")
