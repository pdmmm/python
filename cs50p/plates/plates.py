def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False

    has_number = False

    for i, char in enumerate(s[2:]):
        if i == 0 and char.isdigit() and char == '0':
            return False
        if not char.isalpha() and not char.isdigit():
            return False
        if char.isdigit():
            has_number = True
        if has_number and char.isalpha():
            return False

    return True

main()