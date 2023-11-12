import random

def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 3

        while tries > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries -= 1
            except ValueError:
                print("EEE")
                tries -= 1

        if tries == 0:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in ([1,2,3]):
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level not in ([1,2,3]):
        pass
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10**(level - 1), (10**level) - 1)

if __name__ == "__main__":
    main()
