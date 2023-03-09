"""
Connor Ragland
Lab 06
"""


def print_menu():  # Print user menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


def encoder(password):  # Encode password
    password_list = []
    encoded_password = ''
    for char in password:  # Turn into list
        password_list.append(int(char))
    for idx in range(len(password_list)):
        password_list[idx] += 3  # Add 3 to each digit
        if password_list[idx] > 9:  # If the digit goes over 9 subtract 10
            password_list[idx] -= 10
    for idx in range(len(password_list)):
        encoded_password += str(password_list[idx])
    return encoded_password


def decoder(password):  # Decode encoded_password
    pass


if __name__ == "__main__":
    encoder_run = True
    while encoder_run:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:  # Encode password
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:  # Decode password
            pass
        elif option == 3:  # Exit program
            encoder_run = False
        else:
            print("Invalid input.\n")  # If false option is selected
