# Task 1
user_name = input("What is you name? ")
user_age = input("How old are you? ")
favourite_colour = input("What is your favourite colour? ").lower()
print(f"Thank you {user_name}.")
info_view = input("Would you like to view the information you have given us? (y/n)")
while info_view.lower() not in ["y", "n"]:
    print("Invalid input. Please enter either y or n.")
    info_view = input("Would you like to view the information you have given us? (y/n)")
if info_view.lower() == "y":
    print (f"Your name is {user_name}, you are {user_age} years old and your favourite colour is {favourite_colour}.")
    print("Thank you for your time.")
else:
    print("Thank you for your time.")