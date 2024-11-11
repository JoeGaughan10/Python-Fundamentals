# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Mocha"
# ]

# print(coffee_order)

#---------------------------------------------

# i_spy = [
#     "Camera",
#     "Coffee",
#     "Guitar"
# ]

# print(i_spy[2])

# i_spy[2] = "Bed"

# print(i_spy[2])

# print(len(i_spy))

#---------------------------------------------

# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Mocha"
# ]

# print(coffee_order)

# # Use append to add to a list. This always adds to the end.
# coffee_order.append("Diane- Cappuccino")
# print(coffee_order)

# # Use insert and give the intended index in order to add in a certain position.
# coffee_order.insert(2, "Joseph - Frappe")
# print (coffee_order)

# # Use pop to remove the last item in a list.
# coffee_order.pop()
# print(coffee_order)

# # Use del to remove from a list in a specific position.
# del coffee_order[2]
# print(coffee_order)

# # You can also use .pop() to remove a specific position.
# coffee_order.pop(0)

# ---------------------------------------------------------

# shopping_list = [
#     "apple",
#     "carrot",
#     "pizza",
#     "carrot",
#     "dog food",
#     "orange juice",
#     "egg",
#     "kale",
#     "carrot",
#     "kale",
#     "orange juice",
#     "kale",
#     "toilet roll",
#     "stamps",
#     "noodles",
#     "pasta sauce",
#     "egg",
#     "pasta sauce"
# ]

# print(f"Within this shopping list there are {shopping_list.count("egg")} eggs, {shopping_list.count("kale")} lots of kale, {shopping_list.count("carrot")} carrots and {shopping_list.count("orange juice")} lots of orange juice.")

#-------------------------- Activities ------------------------------

#------------------------ Task 1 ------------------------------------

# favourite_websites = [
#     "https://www.bbc.co.uk/",
#     "https://chatgpt.com/",
#     "https://www.youtube.com/"
# ]

# favourite_websites.extend(["https://www.netflix.com/gb/", "https://open.spotify.com/"]) # .extend allows for multiplt aditions to a list.
# print(favourite_websites)

# favourite_websites.pop(-1)
# print(favourite_websites)

#------------------------ Task 2 -----------------------------------

# favourite_websites = [
#     "https://www.bbc.co.uk/",
#     "https://chatgpt.com/",
#     "https://www.youtube.com/"
# ]

# favourite_websites.remove("https://www.bbc.co.uk/") # .remove removes values by content, not index.
# print(favourite_websites)

# favourite_websites.reverse() # .reverse reverses the order of the items within a list.
# print(favourite_websites)

# favourite_websites.sort() # .sort sorts the items and can be tailored to specific criteria.
# print(favourite_websites)

# print(favourite_websites.count("https://chatgpt.com/")) # .count() counts the number of times an item occurs.

# favourite_websites.extend(["https://www.netflix.com/gb/", "https://open.spotify.com/"]) # .extend extends the list by one or more items.
# print(favourite_websites)

#------------------------------------------------------------------------

# favourite_cars = [
#     "lotus",
#     "porsche",
#     "ferrari"
# ]

# car_guess1 = input("Can you guess one of my 3 favourite car makes? ").lower()

# if car_guess1 in favourite_cars:
#     print("That is one of them! ")
#     car_guess2 = input("Can you guess another? ").lower()
#     if car_guess2 in favourite_cars and car_guess2 != car_guess1:
#         print("Absolutely!")
#         car_guess3 = input("Can you guess the final one? ").lower()
#         if car_guess3 in favourite_cars and car_guess3 != car_guess1 and car_guess3 != car_guess2:
#             print("You got them all! Well Done.")
#         elif car_guess3 == car_guess1 or car_guess3 == car_guess2:
#             print(f"You have already got {car_guess3}!")
#         else:
#             print("No, that is not one of my favourites.")
#     elif car_guess2 == car_guess1:
#         print(f"You have already guessed {car_guess2}!")
#     else:
#         print("No, that is not one of my favourites.")
# else:
#     print("No, that is not one of my favourites.")

# print("Good try!")

#---------------------------- Chat GPT Version ---------------------------------------

favourite_cars = {"lotus", "porsche", "ferrari"}  # Using a set for faster lookup
guessed_cars = set()  # Set to keep track of correct guesses

print("Try to guess my 3 favourite car makes!")

# Loop to allow up to 3 unique guesses
for attempt in range(3):
    car_guess = input("Can you guess one of my favourite car makes? ").lower()

    if car_guess in guessed_cars:
        print(f"You've already guessed correct guess to the set

        if len(guessed_cars) == len(favourite_cars):
            print("You got them all! Well done.")
            break  # Exit loop if all guesses are correct
    else:
        print("No, that is not one of my favourites.")

# End of game message
if len(guessed_cars) < len(favourite_cars):
    print("Good try! Here were my favourite cars:")
    print(", ".join(favourite_cars))
