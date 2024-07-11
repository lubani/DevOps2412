def add_names(names_list, path):
    with open(path, "a+") as f:
        for name in names_list:
            f.write(f"{name}\n")


def print_names(path):
    with open(path, "r") as f:
        for name in f:
            print(f"Hello, {name.strip()}!")


if __name__ == "__main__":
    path = "names.txt"
    add_names(["Nica", "Shelly", "Mor"], path)
    print_names(path)
