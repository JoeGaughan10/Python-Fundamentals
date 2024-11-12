# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

#------------------ Task -------------------

# from datetime import datetime

# while True:
#     birthdate_str = input("Enter your birthday (DD/MM/YYYY) ")

#     try:
#         birthday = datetime.strptime(birthdate_str, "%d/%m/%Y")
#         break
    
#     except ValueError:
#         print("Invalid date format. Please use DD/MM/YYYY")

# today = datetime.now()

# days_alive = (today - birthday).days

# print(f"You have been alive for {days_alive} days.")

#--------------------- Katy's Version --------------------

from datetime import datetime

birthdate = datetime(2002, 2, 13)

current_date = datetime.now()

days_alive = (current_date - birthdate).days

print(f"You have been alive for {days_alive} days.")