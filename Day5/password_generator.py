import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    print("\nWelcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password? ------> ")) 
    nr_symbols = int(input(f"How many symbols would you like? ------> "))
    nr_numbers = int(input(f"How many numbers would you like? ------> "))

    new_password_list = []

    for i in range(0,nr_letters):
        new_password_list.append(letters[random.randint(0,len(letters)-1)])
    for i in range(0,nr_symbols):
        new_password_list.append(symbols[random.randint(0,len(symbols)-1)])
    for i in range(0,nr_numbers):
        new_password_list.append(numbers[random.randint(0,len(numbers)-1)])

    random.shuffle(new_password_list)

    print(f"Your new password is: {''.join(new_password_list)}\n")

while True:
    password_generator()

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P