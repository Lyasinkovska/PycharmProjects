import string


def encrypt_caesar(message: str, key: int = 3):
    alphabet = string.ascii_letters
    encrypted_message = []
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter) + key
            encrypted_letter = alphabet[index % len(alphabet)]
        else:
            encrypted_letter = letter
        encrypted_message.append(encrypted_letter)
    return ''.join(encrypted_message)


if __name__ == '__main__':
    print(encrypt_caesar('Z455a', -5))
