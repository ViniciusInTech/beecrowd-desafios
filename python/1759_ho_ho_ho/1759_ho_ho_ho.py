n = int(input())
message = ""
if n > 1:
    message = "Ho " * (n-1)
    message += "Ho!"
    print(message)
elif n == 1:
    print("Ho!")
else:
    pass