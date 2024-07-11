from get_age import get_user_age


def addition(a, b):
    return a - b


if __name__ == '__main__':
    x = get_user_age()
    y = get_user_age()
    z = get_user_age()
    result = addition(addition(x, y), z)
    print(result)
