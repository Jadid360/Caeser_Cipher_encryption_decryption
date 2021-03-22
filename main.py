# bacically this project is all about encryption and decryption
from art import logo
print(logo)

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
]
# Encrypt Function
def ceaser(start_text,shift_amount,cipher_direction):
    # if shift_number > len(letters):
    #     shift_number =int(shift_number / len(letters))
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in letters:
            position = letters.index(char)
            new_position = position + shift_amount
            end_text += letters[new_position]
            print(new_position)
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


should_continue = True

while should_continue:
    user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    user_message = input("Type your message :").lower()
    shift_amount = int(input("Type your shift number :"))

    shift_amount = shift_amount % 25
    ceaser(start_text=user_message,shift_amount=shift_amount,cipher_direction=user_choice)

    result = input('Would you like to repeat the program again? "Yes" or "No"\n').lower()
    if result=="no":
        should_continue=False
        print("Program ended...")

