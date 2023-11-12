import random
import sys

while True:
    try:
        n = int(input("Level: "))
        if n >= 1:
            random_number = random.randrange(1, n + 1)
            while True:
                try:
                    g = int(input("Guess: "))
                    if g < random_number:
                        print("Too small!")
                    elif g > random_number:
                        print("Too large!")
                    elif g == random_number:
                        print("Just right!")
                        break
                except ValueError:
                    pass
            break
    except ValueError:
        pass
