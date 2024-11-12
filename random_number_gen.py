import random

# print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1, 10))

#------------ Random Integer Game -------------

print("Try to guess 1 number correctly within 10 guesses!")
count = 0
correct_count = 0

while count < 10 and correct_count < 1:
    my_number = int(input("Enter a number between 1 & 10. "))
    random_number = random.randint(1,10)
    if my_number == random_number:
        print(f"{my_number}:{random_number} - Correct!")
        count = count + 1
        correct_count = correct_count + 1
    else:
        print(f"{my_number}:{random_number} - wrong!")
        count = count + 1

if correct_count == 1:
    print("You win!")
else:
    print("Game over!")

