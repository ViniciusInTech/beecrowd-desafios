x, y = map(float, input().split())
z = y - x
r = (z/x) * 100
print(f"{r:.2f}%")