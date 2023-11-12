def remove_vowels(text):
    vowels = "AEIOUaeiou"
    translation_table = str.maketrans('', '', vowels)
    text_without_vowels = text.translate(translation_table)
    return text_without_vowels

def main():
    user_input = input("Input: ")
    text_without_vowels = remove_vowels(user_input)
    print("Output:", text_without_vowels)

if __name__ == "__main__":
    main()