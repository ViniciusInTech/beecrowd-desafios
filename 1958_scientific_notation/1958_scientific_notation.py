def format_scientific_notation(number):
    formatted_number = "{:+.4E}".format(number)

    mantissa, exponent = formatted_number.split('E')

    exponent_sign = exponent[0]
    exponent_value = exponent[1:].zfill(2)

    formatted_number = f"{mantissa}E{exponent_sign}{exponent_value}"

    return formatted_number


number = float(input().strip())

print(format_scientific_notation(number))
