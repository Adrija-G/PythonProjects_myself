def get_key_matrix(key):
    k = 0
    key_matrix = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1
    return key_matrix


def encrypt_message(message_vector, key_matrix):
    cipher_matrix = [[0] for i in range(3)]
    for i in range(3):
        for j in range(1):
            cipher_matrix[i][j] = 0
            for x in range(3):
                cipher_matrix[i][j] += (key_matrix[i][x] *
                                        message_vector[x][j])
            cipher_matrix[i][j] = cipher_matrix[i][j] % 26
    return cipher_matrix


def hill_cipher(message, key):
    key_matrix = get_key_matrix(key)
    message_vector = [[0] for i in range(3)]

    for i in range(3):
        message_vector[i][0] = ord(message[i]) % 65

    cipher_matrix = encrypt_message(message_vector, key_matrix)

    cipher_text = []
    for i in range(3):
        cipher_text.append(chr(cipher_matrix[i][0] + 65))

    print("Ciphertext: ", "".join(cipher_text))


def main():
    message = input("Enter the message (3 characters): ")
    key = input("Enter the key (9 characters): ")

    if len(message) != 3 or len(key) != 9:
        print("Message should be 3 characters long, and the key should be 9 characters long.")
    else:
        hill_cipher(message, key)


if __name__ == "__main__":
    main()

