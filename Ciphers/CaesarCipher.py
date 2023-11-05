def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = (char_code - ord('a') + shift) % 26 + ord('a')
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            encrypted_text += char_code
        else:
            encrypted_text += char

    return encrypted_text


def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)


def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = (char_code - ord('a') + shift) % 26 + ord('a')
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            encrypted_text += char_code
        else:
            encrypted_text += char

    return encrypted_text


def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)


if __name__ == "__main__":
    main()
