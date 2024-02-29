import random
import string

def substitution_cipher(text, key):
    """
    Encrypts the input text using a substitution cipher with the given key.

    Args:
        text (str): The input text to be encrypted.
        key (int): The encryption key.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = 97 if char.islower() else 65
            encrypted_text += chr((ord(char) + key - base) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def generate_random_text(length):
    """
    Generates random text of the specified length.

    Args:
        length (int): The length of the random text to generate.

    Returns:
        str: The randomly generated text.
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_random_key():
    """
    Generates a random encryption key.

    Returns:
        int: The random encryption key.
    """
    return random.randint(-26, 26)

def encrypt(text):
    """
    Encrypts the input text using a substitution cipher with random parameters.

    Args:
        text (str): The input text to be encrypted.

    Returns:
        str: The encrypted text.
    """
    key = generate_random_key()
    cipher_text = substitution_cipher(text, key)
    random_text1 = generate_random_text(random.randint(0, 6))
    random_text2 = generate_random_text(random.randint(0, 6))
    length = len(cipher_text)
    encrypted_text = cipher_text + random_text1 + str(key) + str(length) + random_text2
    return encrypted_text

if __name__ == "__main__":
    text = "ravindu"
    encrypted_text = encrypt(text)
    print("Encrypted value is:", encrypted_text)