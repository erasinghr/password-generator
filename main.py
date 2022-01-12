# Password Generator Project
import random


def password_easy(password):
    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    for i in password:
        print(i, end="")


def password_strong(password):
    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    for i in range(len(password)):
        print(random.choice(password), end="")


def password_generator(nr_letters, nr_numbers, nr_symbols, nr_generator):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = []
    for i in range(nr_letters):
        password.append(random.choice(letters))
    for i in range(nr_symbols):
        password.append(random.choice(symbols))
    for i in range(nr_numbers):
        password.append(random.choice(numbers))
    if nr_generator == 'easy':
        password_easy(password)
    elif nr_generator == 'strong':
        password_strong(password)
    else:
        print(f"Invalid input: Please mention 'easy' or 'strong' without quotes in lowercase")


def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    nr_generator = input(f"What sort of password you want? Reply by typing 'easy' or 'strong' all in lowercase \n")
    password_generator(nr_letters, nr_numbers, nr_symbols, nr_generator)


if __name__ == '__main__':
    main()
