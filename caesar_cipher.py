"""Caesar Cipher Project (freeCodeCamp)"""

import sys
import string

def caesar(text, shift, encrypt=True):

    if not text.isalpha():
        sys.exit("Input text must contain alphabetic characters only.")
    
    if not isinstance(shift, int):
        sys.exit("Shift must be an integer value.")
    
    if shift < 1 or shift > 25:
        sys.exit("Shift must be an integer between 1 and 25.")
    
    alphabet = string.ascii_lowercase
    
    if not encrypt:
        shift = - shift
        
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    response = text.translate(translation_table)
    return response
    
def encrypt(text, shift):
    return caesar(text, shift)
        
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

def main():
    print("-------   CaesarX   -------")
    print("A simple text encryption and decryption program based on the Caesar Cipher technique.")
    print()
    print("What would you have me do?")
    print("1. Encrypt  |  2. Decrypt")
    ch = input(("Your Choice (1/2): "))
    if ch == '1':
        # Encryption
        plain_text = input("Plain Text: ")
        key = int(input("Shift Value: "))
        encrypted_text = encrypt(plain_text, key)
        print("Encrypted Text: ", encrypted_text)
    
    elif ch == '2':
        # Decryption
        encrypted_text = input("Cipher Text: ")
        key = int(input("Shift Value: "))
        decrypted_text = decrypt(encrypted_text, key)
        print("Decrypted Text: ", decrypted_text)
    
    else:
        sys.exit("It seems you don't have anything for me.")

if __name__ == "__main__":
    main()