import inflect
p = inflect.engine()

names =[]
while True:
    try:
        name = input("Name :")
        names.append(name)
    except EOFError:
        print()
        break

farewell_message = p.join(names, final_sep=",")
output = f"Adieu, adieu, to {farewell_message}"

print(output)
