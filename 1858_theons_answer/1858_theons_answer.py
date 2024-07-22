def find_minimum_hits_person():
    N = int(input())
    T = list(map(int, input().split()))
    min_hits = float('inf')
    person_number = -1
    for i in range(N):
        if T[i] < min_hits:
            min_hits = T[i]
            person_number = i + 1
    print(person_number)

find_minimum_hits_person()
