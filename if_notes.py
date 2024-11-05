# These are my if notes

# music = "classical"

# if music == "classical":
#     print("Oh no, not classical again!")
# elif music == "no music":
#     print("Alexa, play some music!")
# elif music == "britpop":
#     print("My second favourite!")
# else:
#     print("I've not heard of this before!")

# -------------------------------------------------

# age = int(input("How old are you? "))

# if age >= 18:
#     print("Yes, I can serve you.")
# else:
#     print("You aren't old enough.")

# -------------------------------------------------

# place = "MCR"
# weather = "Cloudy"

# if place == "MCR" and weather == "Sunny":
#     print("Check again!")
# elif place == "MCR" and weather == "Rain":
#     print("Obvs")
# else:
#     print("What? It isn't raining?")

# ------------------------------------------------

# age =int(input("How old are you? "))
# nationality = input("Are you from the UK? (y/n)")

# while nationality.lower() not in ["y", "n"]:
#     print("Invalid input. Please use y or n")
#     nationality = input("Are you from the UK? (y/n)")

# if age >= 18 and nationality.lower() == "y":
#     print("I can serve you.")
# else:
#     print("I cannot serve you.")

# -------------------- Task 1 ----------------------------

# password = input("Please type a password. ")

# if len(password) < 8:
#     print("Password is too short.")
# else:
#     print(f"Thank you. Your password is {password}.")

# -------------------- Task 2 ----------------------------

# num = int(input("Please enter a number. "))

# if num%3 == 0 or num%5 == 0:
#     print("This number is devisable by 3 or 5.")
# else:
#     print("This number is not divisable by 3 or 5.")

# -------------------- Task 3 ----------------------------

# num = int(input("Please enter a number. "))

# if num%3 == 0 and num%7 == 0:
#     print("fizzbuzz")
# elif num%3 == 0:
#     print("fizz")
# elif num%7 == 0:
#     print("buzz")
# else:
#     print(num)

# -------------------- Task 4 ----------------------------

# answer = input("What is the capital of England? ")

# if answer.lower() == "london":
#     print(f"Correct! The answer is {answer.capitalize()}.")
# else:
#     print(f"Incorrect, the answer is 'London', not {answer}.")

# -------------------- Task 5 ----------------------------

# word = input("Please type any word. ")
# word_length = len(word)

# if word.lower()[0] == word.lower()[-1]:
#     print("True")
# else:
#     print("False")

# -------------------- Task 6 ----------------------------

# word = input("Please type any word. ")
# word_reversed = ''.join(reversed(word))

# if word.lower() == word_reversed.lower():
#     print("True")
# else:
#     print("False")