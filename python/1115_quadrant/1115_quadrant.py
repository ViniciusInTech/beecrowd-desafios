while True:
    x, y = map(int, input().split(" "))
    if 0 == x or 0 == y:
        break
    elif x > 0 and y > 0:
        print("primeiro")
    elif x > 0 and y < 0:
        print("quarto")
    elif x < 0 and y < 0:
        print("terceiro")
    elif x < 0 and y > 0:
        print("segundo")