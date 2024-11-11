# capital_cities = {
#     "England" : "London",
#     "Scotland" : "Edinburgh",
#     "Wales" : "Cardiff",
#     "Northern Ireland" : "Belfast",
#     "Ireland" : "Mayo",
#     "Ireland" : "Dublin" # Duplicates overwrite
# }

# print(capital_cities["England"]) # Result is 'London'

# print(f"The capital city of England is {capital_cities["England"]} and the capital city of Ireland is {capital_cities["Ireland"]}.")

#-----------------------------------------------------------------------------------------------------------------------------------------------

# baby_animals = {
#     "Gecko" : "Baby Gecko",
#     "Whale" : "Calf",
#     "Swan" : "Signet"
# }

# baby_animals["Gecko"] = "Hatchling"

# print(baby_animals)
# print(baby_animals.keys()) # Displays the keys (first of the pair)
# print(baby_animals.values()) # Displays the values (second of the pair)
# print(baby_animals.items()) # Displays both keys and values.

# # print(baby_animals["Turtle"]) # Shows an error
# print(baby_animals.get("Turtle")) # Displays 'None'
# print(baby_animals.get("Turtle", "This animal is not within the dictionary. Sorry!")) # Displays 'This animal is not within the dictionary. Sorry!'.

# baby_animals.setdefault("Dog", "Puppy") # Adds to the end of the dictionary.
# print(baby_animals)

# baby_animals.setdefault("Gecko", "Hatchling") # Recognises duplication and does not add.
# print(baby_animals)

#------------------------- Activities ------------------------------------------------------------------------------------------------------------------------------------

#-------------------------- Task 1 ----------------------------------------

# languages = {
#     "England" : "English",
#     "Spain" : "Spanish",
#     "Ethiopia" : "Amharic",
#     "Iran" : "Farsi"
# }

# print(languages)

#-------------------------- Task 2 ------------------------------------------

baby_animals = {
    "Gecko" : "Hatchling",
    "Whale" : "Calf",
    "Swan" : "Signet"
}

searched_animal = input("Please search for an animal to discover the name of it's young. ").capitalize()

if searched_animal in baby_animals:
    print(f"A {searched_animal.lower()}'s young is a {baby_animals[searched_animal].lower()}.")
else:
    print("Sorry, that animal is unknown.")

inquire = True

while inquire == True:
    search_again = input("Would you like to search for another animal? (y/n) ")
    if search_again.lower() == "y":
        searched_animal = input("Please search for an animal to discover the name of it's young. ").capitalize()
        if searched_animal in baby_animals:
            print(f"A {searched_animal.lower()}'s young is a {baby_animals[searched_animal].lower()}.")
        else:
            print("Sorry, that animal is unknown.")
    elif search_again.lower() == "n":
        print("I hope that was helpful!")
        inquire = False
    else:
        print ("Invalid response. Please try again using 'y' or 'n'.")

# --------------------------- This starts with asking for another search ------------------------------

# ---------------------------- Chat GPT Version ---------------------------------

# baby_animals = {
#     "Gecko": "Hatchling",
#     "Whale": "Calf",
#     "Swan": "Signet"
# }

# # Initial search
# searched_animal = input("Please search for an animal to discover the name of its young: ").capitalize()

# # Check if the animal exists in the dictionary
# if searched_animal in baby_animals:
#     print(f"A {searched_animal.lower()}'s young is a {baby_animals[searched_animal].lower()}.")
# else:
#     print("Sorry, that animal is unknown.")

# # Inquiry loop
# inquire = True

# while inquire:
#     search_again = input("Would you like to search for another animal? (y/n) ").lower()
    
#     if search_again == "y":
#         searched_animal = input("Please search for an animal to discover the name of its young: ").capitalize()
        
#         # Check if the animal exists in the dictionary
#         if searched_animal in baby_animals:
#             print(f"A {searched_animal.lower()}'s young is a {baby_animals[searched_animal].lower()}.")
#         else:
#             print("Sorry, that animal is unknown.")
    
#     elif search_again == "n":
#         print("I hope that was helpful!")
#         inquire = False
    
#     else:
#         print("Invalid response. Please try again using 'y' or 'n'.")

#-------------------------- Still not working. --------------------------------------
