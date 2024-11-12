import random
from colorama import Fore, Style

good_responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes definitely.",
                 "You may rely on it."]

bad_responses = ["Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful.",
                ]

repeat = "y"
while repeat == "y":
    question = input("Ask a question. ")
    if random.randint(1,2) % 2 == 0:
        print(Fore.GREEN+f"{random.choice(good_responses)}")
        print(Style.RESET_ALL)

    else:
        print(Fore.RED+f"{random.choice(bad_responses)}")
        print(Style.RESET_ALL)

    repeat = input("Any more questions? (y/n) ").lower()
    while repeat != "y" and repeat != "n":
        print("Invalid input.")
        repeat = input("Any more questions? (y/n) ").lower()

print("Thank you for speaking with the 8 Ball.")