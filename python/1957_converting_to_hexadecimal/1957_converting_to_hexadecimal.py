def decimal_to_hexadecimal(decimal_number):
    hex_string = hex(decimal_number)[2:]
    hex_string = hex_string.upper()
    return hex_string

decimal_number = int(input().strip())

print(decimal_to_hexadecimal(decimal_number))
