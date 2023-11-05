def atbash_cipher(text):
    result = []

    for char in text:
        if char.isalpha():
            if char.islower():
                offset = ord('a')
                result.append(chr(ord('z') - (ord(char) - offset)))
            else:
                offset = ord('A')
                result.append(chr(ord('Z') - (ord(char) - offset)))
        else:
            result.append(char)

    return ''.join(result)

def input_text():
    text = input("Enter the text to encrypt with the Atbash cipher: ")
    return text

def encrypt_text(text):
    encrypted_text = atbash_cipher(text)
    return encrypted_text

def output_text(encrypted_text):
    print("Encrypted text:", encrypted_text)

def main():
    text = input_text()
    encrypted_text = encrypt_text(text)
    output_text(encrypted_text)

if __name__ == "__main__":
    main()
