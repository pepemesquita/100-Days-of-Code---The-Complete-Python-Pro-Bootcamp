alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

word_encrypted = []

def encrypt(original_text, shift_amount):
    for letter in original_text:
        letter_index = alphabet.index(letter) + shift_amount
        letter_index %= len(alphabet)
        word_encrypted.append(alphabet[letter_index])

    print(f"Here is the encoded result: {"".join(word_encrypted)}")

encrypt(text, shift)