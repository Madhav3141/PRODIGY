# 1).Create a python program that can encrypt decrypt text using ceasar cipher algorithm, Allow user to input a message and a shift value to perform encryption and decryption

while True:
    choice = input("Type 'encrypt' to encrypt, or 'decrypt' to decrypt, or 'exit' to quit: ").lower()


    if choice == exit:
        print("Bye bye beta...")
        time.sleep(2)
        break

    if choice not in ['encrypt','decrypt']:
        print("Invalid choice please enter as per given data!")
        continue

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    result = ""

    if choice.lower() == 'decrypt':
        shift = -shift

    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                ascii = ord('a')
            else:
                ascii = ord('A')
            new_char = chr(ascii + (ord(char.lower()) - ascii + shift_amount) % 26 )
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char

    print(f"Your encrypt / decrypt message is: {result}")
