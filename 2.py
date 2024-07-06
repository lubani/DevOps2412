"""
Luba Ira
email lubacareer@gmail.com
Task 2
"""

from operator import concat


class Task2:

    def printHello(self):
        print("Hello")

    def calculate(self):
        print("5 + 3.2 = ", 5 + 3.2)

    def my_name(self, name):
        print(name)

    def div_two(self, a):
        print(f"{a} / 2 = ", a / 2)

    def add(self, a, b):
        return a + b

    def concatenate(self, a, b):
        return concat(a, b)

    def get_num(self):
        num = input("Please enter a number: ")
        self.sum_num(num)

    def sum_num(self, num):
        sum = 0
        for digit in str(num):
            sum += int(digit)
        print(f"The digits' sum of {num} is {sum}")


if __name__ == "__main__":
    print("A. ")
    X, Y = input("Please enter integers for X and Y, separated by spaces: ").strip().split(' ')
    if X > Y:
        print("BIG")
    elif X < Y:
        print("small")
    else:
        pass

    print("B. ")
    for i in range(5):
        print(i)

    print("C. ")
    A = input("Please enter a number between 1 and 4: ")
    match A:
        case "1":
            print("Summer")
        case "2":
            print("Winter")
        case "3":
            print("Fall")
        case "4":
            print("Spring")
        case _:
            print("Not a number between 1 and 4")

    print("D. ")
    count = 1
    while count < 11:
        print(count)
        count += 1
    print(f"The loop ran {count - 1} times")

    print("E. ")
    my_inf = {"age": 30, "letter_lname": 'L', "NIS_dollar": 0.27, "abroad": True, "apt_no": 22}
    print(my_inf)
    print("What happens if I sum age and currency?")
    print(my_inf["age"] + my_inf["NIS_dollar"])

    print("F. ")
    phone_num = input("Please enter a phone number: ")
    print("Phone Number ", phone_num)

    print("G. ")
    GHIM = Task2()
    GHIM.printHello()
    GHIM.calculate()
    print("H. ")
    GHIM.my_name("John")
    GHIM.div_two(5)
    print("I. ")
    print("5 + 5 = ", GHIM.add(5, 5))
    print(GHIM.concatenate("Hello ", "World"))

    print("J.")
    for i in range(6):
        for _ in range(i):
            print('*', end='')
        print("\n")

    print("K.")
    for i in range(7):
        k2 = 7 - i
        for j in range(7):
            if j == i or j == 7 - i:
                print('*', end='')
            else:
                print('  ', end='')
        print("\n")

    GHIM.get_num()
