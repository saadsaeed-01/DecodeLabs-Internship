"""
Project 2: Basic Encryption & Decryption
Implements a Caesar cipher for simple text encryption and decryption.
"""


def encrypt(text, shift):
    """
    Encrypts text using Caesar cipher.
    
    Args:
        text (str): The text to encrypt
        shift (int): The number of positions to shift each character
    
    Returns:
        str: The encrypted text
    """
    encrypted = ""
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            if char.isupper():
                # Shift uppercase letters
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Shift lowercase letters
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Keep non-alphabetic characters unchanged
            encrypted += char
    
    return encrypted


def decrypt(text, shift):
    """
    Decrypts Caesar cipher encrypted text.
    
    Args:
        text (str): The encrypted text to decrypt
        shift (int): The number of positions that were shifted (same as encryption)
    
    Returns:
        str: The decrypted text
    """
    # Decryption is just encryption with negative shift
    return encrypt(text, -shift)


def main():
    """Main function to run the encryption/decryption program."""
    
    print("=" * 50)
    print("Caesar Cipher: Encryption & Decryption")
    print("=" * 50)
    
    # Get user input
    user_text = input("\nEnter the text to encrypt: ")
    
    while True:
        try:
            shift_value = int(input("Enter the shift value (1-25): "))
            if 1 <= shift_value <= 25:
                break
            else:
                print("Please enter a value between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print("\n" + "-" * 50)
    
    # Encrypt the text
    encrypted_text = encrypt(user_text, shift_value)
    print(f"\nOriginal Text:  {user_text}")
    print(f"Shift Value:    {shift_value}")
    print(f"Encrypted Text: {encrypted_text}")
    
    # Decrypt the text
    decrypted_text = decrypt(encrypted_text, shift_value)
    print(f"Decrypted Text: {decrypted_text}")
    
    print("\n" + "-" * 50)
    
    # Verify encryption/decryption
    if decrypted_text == user_text:
        print("✓ Encryption and decryption successful!")
    else:
        print("✗ Error in encryption/decryption process!")
    
    print("=" * 50)


if __name__ == "__main__":
    main()
