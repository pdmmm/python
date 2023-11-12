def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))

            if x < 0 or y < 0 or x > y:
                raise ValueError

            percentage = round((x / y) * 100)

            if percentage <= 1:
                print("E")
                break
            elif percentage >= 99:
                print("F")
                break
            else:
                print(f"{percentage}%")
                break
        except (ValueError, ZeroDivisionError):
            pass
main()