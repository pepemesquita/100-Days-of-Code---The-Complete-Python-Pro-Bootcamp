alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(encode_or_decode, original_text, shift_amount):
    original_text = ""

    for letter in original_text:
        if encode_or_decode == "decode": #Always is "encode", but verifies the input user, if input is "decode" the number is negative
            shift_amount *= -1

        letter_index = alphabet.index(letter) + shift_amount # The more with less = less
        letter_index %= len(alphabet)
        original_text += alphabet[letter_index]

    print(f"Here is the {encode_or_decode} result: {original_text}")

caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

'''
def encrypt(original_text, shift_amount):
    word_encrypted = ""

    for letter in original_text:
        letter_index = alphabet.index(letter) + shift_amount
        letter_index %= len(alphabet)
        word_encrypted += alphabet[letter_index]

    print(f"Here is the encoded result: {word_encrypted}")

def decrypt(original_text, shift_amount):
    word_decrypted = ""



    print(f"Here is the decoded result: {word_decrypted}")
'''