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

favourite_websites = [
    "https://www.bbc.co.uk/",
    "https://chatgpt.com/",
    "https://www.youtube.com/"
]

favourite_websites.remove("https://www.bbc.co.uk/") # .remove removes values by content, not index.
print(favourite_websites)

favourite_websites.reverse() # .reverse reverses the order of the items within a list.
print(favourite_websites)

favourite_websites.sort() # .sort sorts the items and can be tailored to specific criteria.
print(favourite_websites)

print(favourite_websites.count("https://chatgpt.com/")) # .count() counts the number of times an item occurs.

favourite_websites.extend(["https://www.netflix.com/gb/", "https://open.spotify.com/"]) # .extend extends the list by one or more items.
print(favourite_websites)