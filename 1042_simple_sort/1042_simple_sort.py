a, b, c = map(int, input().split(" "))

def order(a, b):
    if a > b:
        return b, a
    return a, b

a_, b_ = order(a, b)
a_, c_ = order(a_, c)
b_, c_ = order(b_, c_)

print(a_)
print(b_)
print(c_)
print()

print(a)
print(b)
print(c)




