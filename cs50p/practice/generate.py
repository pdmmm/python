import random

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = input("What is your name?: ").split()
random.shuffle(cards)
shuffled_card = " ".join(cards)
print(shuffled_card)
