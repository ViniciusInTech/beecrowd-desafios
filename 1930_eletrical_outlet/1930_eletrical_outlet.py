def max_devices(T1, T2, T3, T4):
    total_outlets = T1 + T2 + T3 + T4 - 3
    return total_outlets

T1, T2, T3, T4 = map(int, input().strip().split())

print(max_devices(T1, T2, T3, T4))
