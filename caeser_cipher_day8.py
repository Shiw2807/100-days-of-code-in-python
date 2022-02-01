alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caeser(start_text, shift_amount, cipher_direc):
    end_text = ""
    if cipher_direc == 'decode':
      shift_amount *= -1
    for char in start_text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        end_text+= char
    print(f"The {cipher_direc}d text is {end_text}")


should_continue=True
while should_continue:
  direction = input("Enter 'encode' to encrypt, 'decode' to decypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type your shift number:\n"))

  shift=shift % 25
  caeser(start_text=text, shift_amount=shift, cipher_direc=direction)

  result = input('Would you like to repeat the program again? "Yes" or "No"\n').lower()
  if result=="no":
    should_continue=False
    print("The program has ended😊\nGoodbye!")