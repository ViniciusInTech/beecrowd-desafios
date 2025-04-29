seconds = int(input())

seconds_conversion = {
    3600: 0,
    60: 0,
    1: 0
}

for conversion in seconds_conversion:
    tempo = seconds // conversion
    if tempo > 0:
        seconds -= tempo*conversion

    seconds_conversion[conversion] = tempo

print(f"{seconds_conversion[3600]}:{seconds_conversion[60]}:{seconds_conversion[1]}")
