#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    p = 0
    if type(roman_string) == str and roman_string:
        roman_string = roman_string[::-1]
        for i in roman_string:
            if roman[i] >= p:
                num += roman[i]
            else:
                num -= roman[i]
            p = roman[i]
    return (num)
