while True:
    number = int(input())
    if number == 0:
        break
    output = ""
    for i in range(number):
        i += 1
        output+= f'{i} '
    print(output.strip())