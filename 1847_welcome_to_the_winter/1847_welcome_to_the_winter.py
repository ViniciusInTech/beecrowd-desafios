def determine_mood(A, B, C):
    if (A > B and B <= C):
        return ":)"
    elif (A < B and B >= C):
        return ":("
    elif (A < B and C - B >= B - A):
        return ":)"
    elif (A < B and C - B < B - A):
        return ":("
    elif (A > B and B - C < A - B):
        return ":)"
    elif (A > B and B - C >= A - B):
        return ":("
    elif (A == B and B < C):
        return ":)"
    elif (A == B and B >= C):
        return ":("

a,b,c = map(int, input().split())
print(determine_mood(a,b,c))