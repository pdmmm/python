def main():
    coke_price = 50
    accepted_coins = [25, 10, 5]
    amount_due = coke_price
    inserted_coins = 0

    while amount_due > 0:
        try:
            coin = int(input("Insert Coin: "))
            if coin in accepted_coins:
                inserted_coins += coin
                amount_due -= coin
                if amount_due > 0:
                    print(f"Amount Due: {amount_due}")
                else:
                    change = inserted_coins - coke_price
                    print(f"Change Owed: {change}")
                    break
            else:
                print(f"Amount Due: {amount_due}")
        except ValueError:
            break
main()