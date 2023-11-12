def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_"
        snake_case += char.lower()
    if snake_case.startswith("_"):
        snake_case = snake_case[1:]
    return snake_case

def main():
    camel_case_variable = input("camelCase: ")
    snake_case_variable = camel_to_snake(camel_case_variable)
    print(":", snake_case_variable)

if __name__ == "__main__":
    main()