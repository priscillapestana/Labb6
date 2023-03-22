# encode, should add 3 to each individual number
def encode(password):
    encoded_password = ''
    for num in password:
        encoded_password += str((int(num) + 3) % 10)
    return encoded_password

# partner will complete
def decode(encoded_password):
    pass

# main function, prints menu, runs encode
def main():
    while True:
        print('Menu')
        print('-------------')
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print('')
        option = int(input('Please enter an option: '))

        if option == 1: # runs encode()
            password = (input('Please enter your password to encode: '))
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
            print('')
            continue

        elif option == 2: # runs decode()
            original_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {original_password}')
            print('')
            continue

        elif option == 3: # exits loop
            break

# runs main
if __name__ == "__main__":
    main()