class NegativeAgeError(Exception):
    """Exception raised for negative user age."""

    def _init_(self, age, message="Age cannot be negative"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def _str_(self):
        return f"{self.message}: {self.age}"


def get_user_age():
    try:
        user_age = int(input("enter age: "))
        if user_age < 0:
            raise NegativeAgeError("Negative user age")
        return user_age
    except NegativeAgeError as e:
        print(e)

