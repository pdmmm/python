expression = input("Expression: ")
x, operator, z = expression.split()
x = float(x)
z = float(z)

result = 0.0

if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    if z != 0:
        result = x / z
    else:
        print("Error: Division by zero.")
        exit()
else:
    print("Error: Invalid operator.")
    exit()

print(f"{result:.1f}" )