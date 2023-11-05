def rail_fence_cipher_encrypt(text, rails):
    fence = [[' ' for _ in range(len(text))] for _ in range(rails)]

    row, col, direction = 0, 0, 1

    for char in text:
        fence[row][col] = char
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
        col += 1

    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text


def rail_fence_cipher_decrypt(text, rails):
    fence = [[' ' for _ in range(len(text))] for _ in range(rails)]

    row, col, direction = 0, 0, 1

    for _ in range(len(text)):
        fence[row][col] = '*'
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
        col += 1

    index = 0
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] == '*' and index < len(text):
                fence[i][j] = text[index]
                index += 1

    row, col, direction = 0, 0, 1
    decrypted_text = []

    for _ in range(len(text)):
        decrypted_text.append(fence[row][col])
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
        col += 1

    return ''.join(decrypted_text)


def main():
    text = input("Enter the text: ")
    rails = int(input("Enter the number of rails: "))

    encrypted_text = rail_fence_cipher_encrypt(text, rails)
    decrypted_text = rail_fence_cipher_decrypt(encrypted_text, rails)

    print("Encrypted text:", encrypted_text)
    print("Original text (after decryption):", decrypted_text)


if __name__ == "__main__":
    main()

