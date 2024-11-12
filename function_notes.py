# def say_hello():
#     print("Hello.")

# say_hello()

# def say_goodbye():
#     print("Goodbye.")

# say_goodbye()

# def say_something(something):
#     print(f"{something*2}")

# something = int(input("Enter a number. "))

# say_something(something)

# def cash_withdrawal(amount, accnum):
#     print(f"You have withdrawn £{amount} from account number {accnum}.")

# cash_withdrawal(300, 12345678)

# drink = input("Which drink would you like? ")
# size = input("What size will that be? ")

# def take_order(size, drink):
#     print(f"You have ordered a {size} {drink}. ")

# take_order(size, drink)

# drink = input("Which drink would you like? ")
# size = input("What size will that be? ")

# ---------------- Katy's Input Version ------------------

# def take_order(size, drink):
#     print(f"You have ordered a {size} {drink}. ")

# take_order(input("What size will that be? "), input("Which drink would you like? "))

# -------------------------------------------------------

def check_order(drink, size):
    input_check = True
    count = 0
    while input_check == True:
        
        order_check = input(f"You have ordered a {size} {drink}. Is this correct? (y/n) ")
        input_check = True

        if order_check.lower() == "y" and count == 0:
            print("Perfect.")
            input_check = False
        elif order_check.lower() == "y" and count > 0:
            print("Sorted. I'm very sorry for the incovinience.")
            input_check = False
        elif order_check == "n":
            print("Uh oh.")
            input_check = True
            drink = input("Which drink was it again? ").lower()
            size = input("And what size did you want? ").lower()
            count = count + 1
        else:
            print("What are you on about?")
            input_check = True


check_order(drink = input("Which drink would you like? ").lower(), size = input("What size will that be? ").lower())