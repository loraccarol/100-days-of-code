alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(encode_or_decode, original_text, shift_amount):
    cipher_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            new_index = alphabet.index(letter) + shift_amount
            new_index %= len(alphabet)
            cipher_text += alphabet[new_index]

    print(cipher_text)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number\n"))

caeser(direction, text, shift)