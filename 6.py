
def get_user_age():
    try:
        user_age = int(input("Enter your age: "))
        if user_age < 0:
            raise ValueError("Age cannot be negative")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    get_user_age()
