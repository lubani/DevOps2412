"""
Luba Ira
email lubacareer@gmail.com
phone 0527044577
"""

import math


def rad_to_deg(rad):
    return rad * 180 / math.pi


def sort_list(list1, order=None):
    match order:
        case "asc":
            list1.sort()
        case "desc":
            list1.sort(reverse=True)
        case None:
            pass
    return list1


def dec_to_bin(dec):
    # convert a decimal number to binary
    return bin(dec)[2:]


def dec_to_bin_manual(dec):
    if dec == 0:
        return "0"
    binary = ''
    while dec > 0:
        binary = str(dec % 2) + binary
        dec = dec // 2
    return binary


def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count


def hide_digits(string):
    # Hide all the digits in the string except the last 4
    temp = ""
    if len(string) < 4:
        return "The number is too short to hide"
    for i, digit in enumerate(string):
        if i not in range(len(string) - 4, len(string)):
            temp += "*"
        if i in range(len(string) - 4, len(string)):
            temp += digit
    return temp


def count_XOs(string):
    count_X, count_O = 0, 0
    for letter in string:
        if letter == "X":
            count_X += 1
        if letter == "O":
            count_O += 1
    if count_X == count_O:
        return True
    else:
        return False


def calculator(integer, integer2, operator):
    match operator:
        case "+":
            return integer + integer2
        case "-":
            return integer - integer2
        case "*":
            return integer * integer2
        case "/":
            return integer / integer2


def discount(full_price, discount_precentage):
    return full_price - ((100 * discount_precentage) / full_price)


def double_character(string):
    str2 = ""
    for letter in string:
        for i in range(2):
            str2 += letter
    return str2


if __name__ == "__main__":
    print(f"{math.pi / 2} radians is {rad_to_deg(math.pi / 2)} degrees")
    my_list = [5, 3, 4, 8, 9, 12, 54, 23, 76, 14]
    print(f"{my_list} sorted is {sort_list(my_list, order="asc")}")
    print(f"The decimal {42} is {dec_to_bin(42)} in binary")
    print(f"The decimal {42} is {dec_to_bin_manual(42)} in binary")
    string = "Hello There"
    print(f"The number of vowels in {string} is {count_vowels(string)}")
    revealed = "55555555555"
    hidden = hide_digits(revealed)
    print(f"Secret number is {revealed} and hidden is: {hidden}")
    string2 = "XOXOXOXOXO"
    print(f"Is the number of X's and O's equal in {string2}? {count_XOs(string2)}")
    a, b = 2, 3
    operator = "*"
    print(f"{a} {operator} {b} = {calculator(a, b, operator)}")
    price, discount_ratio = 100, 25
    print(f"Price {price} after discount of {discount_ratio}% is {discount(price, discount_ratio)}")
    str2 = "What is up?"
    print(f"The doubled characters of {str2} is {double_character(str2)}")

