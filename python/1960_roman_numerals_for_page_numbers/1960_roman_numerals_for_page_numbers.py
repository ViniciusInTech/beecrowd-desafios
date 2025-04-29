def int_to_roman(n):
    roman_numerals = [
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result = ''

    for value, numeral in roman_numerals:
        while n >= value:
            result += numeral
            n -= value

    return result


n = int(input().strip())
print(int_to_roman(n))
