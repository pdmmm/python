name = input("What is the Answer to the Great Question of Live, the Universe, and Everything?")

name = name.replace(" ", "")

match name.lower():
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")