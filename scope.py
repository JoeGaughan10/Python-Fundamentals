#--------------------- Task 1 ----------------------

# def happy_birthday_song(name):
#     print(f"Happy Birthday to you,\nHappy Birthday to you,\nHappy Birthday dear {name},\nHappy Birthday to you!")

# happy_birthday_song(name = input("What is your name? "))

#--------------------- Task 2 ----------------------

order_count = 1

def take_order(topping, size):
    global order_count
    print(f"Order #{order_count}: {size}' pizza with {topping}.")
    order_count = order_count + 1

take_order(input("What type of pizza would you like? "), input("What size will that be? "))
take_order(input("What type of pizza would you like? "), input("What size will that be? "))

#-------------------- Task 3 ----------------------

def find_mean(dataset):
    total = 0
    for i in dataset:
        total = total + i
    mean = total/len(dataset)
    print(mean)

dataset = [34,67,5,81,2,45,9,23,55,41,42,84,109, 109, 109]
find_mean(dataset)