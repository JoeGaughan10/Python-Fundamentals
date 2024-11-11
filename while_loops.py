# answer = input("Who ordered the cortado? ").capitalize()

# while answer != "Alex":
#     print("incorrect")
#     answer = input("Who ordered the cortado?").capitalize()
# else:
#     print("Enjoy your coffee!")

#---------------- Tasks ----------------

# Task 1

# for i in range(13):
#     print("Hello World")

# While loop altenative
# counter  = 0

# while counter < 13:
#     print(f"Hello World ({counter})")
#     counter = counter + 1

# print("That should be 13 outputs.")

# Task 2

# counter = 1
# while counter < 13:
#     for num in range (1,13):
#         print(f"{num} X {counter} = {num*counter}")
#     counter = counter + 1
#     print("")

# print("That should be all multiplication tables up to 12.")

# Task 3

username = "un"
password = "pw"

username_check = input("Enter your username: ")
password_check = input("Enter your password: ")

while username != username_check and password != password_check:
    print("Incorrect. Please try again")
    username_check = input("Enter your username: ")
    password_check = input("Enter your password: ")

print("Correct. You may enter.")
