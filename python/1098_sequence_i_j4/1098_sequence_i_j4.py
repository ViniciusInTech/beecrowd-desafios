i = 0
while i <= 2.0:
    j = 1
    for _ in range(3):
        i_string = f"{int(i)}" if i == int(i) else f"{i:.1f}"
        j_string = f"{int(j+i)}" if (j+i) == int(j+i) else f"{j+i:.1f}"
        print(f"I={i_string} J={j_string}")
        j += 1
    i = round(i + 0.2, 1)