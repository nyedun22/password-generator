import random
#1 variables (letters, numbers and symbols) to use for password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
#2 user input for how long they want password to be (including how many elements from each variable)
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#3 for loops to randomly select elements from each variable based on outcome of user input
for letter in letters:
    pw_letter = random.sample(letters, nr_letters)
for number in numbers:
    pw_number = random.sample(numbers, nr_numbers)
for symbol in symbols:
    pw_symbol = random.sample(symbols, nr_symbols)

#4 combine to create password
password = (pw_letter + pw_number + pw_symbol)
#5 print password elements in random order using random.shuffle()
random.shuffle(password)
#remove list formatting and print final randomly generated password
password = "".join(password)
print(password)
