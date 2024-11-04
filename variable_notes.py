# test_string = "All Around The World"
# print(test_string[7].upper())

# my_name = "Joe"
# print(my_name)

# my_name = "Joe"
# my_age = 22
# is_a_leaner = False
# favourite_drink = "latte"

# print (favourite_drink)
# print("My favourite drink is", favourite_drink)
# print(my_name, "'s favourite drink is", favourite_drink)

# print("My favourite drink is a " + favourite_drink + ".")
# print(my_name + "'s favourite drink is a " + favourite_drink + ".")

# print("My name is " + my_name + ". I am " + my_age + " years old. My favourite drink is a " + favourite_drink + ".")
# print("My name is " + my_name + ". I am " + str(my_age) + " years old. My favourite drink is a " + favourite_drink + ".")

# print("{} is {} years old, and his favourite drink is a {}.".format(my_name, my_age, favourite_drink))
# print(f"{my_name} is {my_age} years old, and his favourite drink is a {favourite_drink}.")

# --------------------- Input Code ----------------------

# my_name = input("Type you name here: ")
# print(f"Hello {my_name}.")
# print(type(my_name))

# balance = 100
# amount_to_withdraw = 20
# print(balance)
# balance = balance - amount_to_withdraw
# print(balance)

# print("Type in two numbers to multiply them.")
# num1 = int(input("Number 1:"))
# num2 = int(input("Number 2:"))
# print(f"Number 1 multiplied by number 2 is {num1*num2}")

balance = 100
amount_to_withdraw = input("Amount required: ")
print(f"Current balance is £{balance}")
balance = int(balance) - int(amount_to_withdraw)
print(f"New balance is £{balance}")
print("Thank you.")
