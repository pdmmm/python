from collections import defaultdict

grocery_list = defaultdict(int)

try:
    while True:
        item = input().strip().lower()
        if not item:
            continue
        grocery_list[item] += 1

except EOFError:
    pass

sorted_items = sorted(grocery_list.keys(), key=lambda x: x.lower())

for item in sorted_items:
    count = grocery_list[item]
    print(f"{count} {item.upper()}")
