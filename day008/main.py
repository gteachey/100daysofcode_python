from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(user_text, shift_amount):
    #e.g.
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    cipher_text = ""
    if direction.lower() != 'encode' and direction.lower() != 'decode':
        print("Please enter 'encode' or 'decode' for this to work!")
        return "Failed!"
    elif direction.lower() == 'encode':
        for char in user_text.lower():
            if char in alphabet:
                new_index = (alphabet.index(char) + shift_amount) % 26
                cipher_text += alphabet[new_index]
            else:
                cipher_text += char
    else:
        for char in user_text.lower():
            if char in alphabet:
                new_index = (alphabet.index(char) - shift_amount) % 26
                cipher_text += alphabet[new_index]
            else:
                cipher_text += char
    return cipher_text


print(f"The encoded text is {caesar(user_text=text, shift_amount=shift)}")
