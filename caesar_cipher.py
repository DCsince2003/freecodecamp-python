"""Caesar Cipher Project (freeCodeCamp)

This project handles:
 - Encryption 
 - Decryption
 using Caesar Cipher Technique
"""

# sys module to utilise its exit() function
# string module to use its ascii_lowercase attribute
import sys
import string

def caesarx(text, shift, encryption = True):
    """Encrypts or decrypts text using the Caesar cipher.
    Args:
        text (str): The input text to be processed
        shift (int): The number of positions to shift each letter.
        encrypt (bool, optional): whether to encrypt or decrypt. Defaults to True.
    Returns:
        str: The resulting encrypted or decrypted text.
    """

    # Ensure valid text and shift value is used
    if not text.isalpha():
        sys.exit("Input text must contain alphabetic characters only.")
    if not isinstance(shift, int):
        sys.exit("Shift must be an integer value.")
    if shift < 1 or shift > 25:
        sys.exit("Shift must be an integer between 1 and 25.")
    if not encryption:
        shift = - shift
    
    # Generate the shifted alphabet mapping for the cipher
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Map both lowercase and uppercase variations to a single translation table
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    # Efficiently swap characters using mapping_table
    return text.translate(translation_table)

def encrypt(text, shift):
    """Encrypts text using a Caesar cipher shift.
    Args:
        text (str): The plaintext to encrypt.
        shift (int): The number of positions to shift each letter.
    Returns:
        str: The encrypted ciphertext.
    """
    return caesarx(text, shift)
    
def decrypt(text, shift):
    """Decrypts text using a Caesar cipher shift.
    Args:
        text (str): The ciphertext to decrypt.
        shift (int): The number of positions to shift each letter.
    Returns:
        str: The decrypted plaintext.
    """
    return caesarx(text, shift, encryption = False)

def main():
    print("----------     CaesarX     ----------")
    print("A simple text encryption and decryption program \nbased on the Caesar Cipher technique.")
    print()
    print("What would you have me do?")
    print("1. Encrypt  |  2. Decrypt")

    ch = input(("Your Choice (1/2): "))
    if ch == '1':
        # Encryption
        plain_text = input("Plain Text: ")
        shift = int(input("Shift Value: "))
        encrypted_text = encrypt(plain_text, shift)  # Shift forward for encryption
        print("Encrypted Text: ", encrypted_text)
    
    elif ch == '2':
        # Decryption
        cipher_text = input("Cipher Text: ")
        shift = int(input("Shift Value: "))
        decrypted_text = decrypt(cipher_text, shift)  # Shift backwards for decryption
        print("Decrypted Text: ", decrypted_text)
    
    else:
        sys.exit("It seems you don't have anything for me.")

if __name__ == "__main__":
    main()