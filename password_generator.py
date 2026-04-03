import string
import random
import os
import time
from colorama import Fore, Style

try:
	chars = string.ascii_letters + string.digits + "!@#$%^&*"

	length = int(input("Enter passsowrd lenght: "))
	stuff_password = input("For what this password: ")

	password = "".join(random.choice(chars) for i in range(length))

	print(f"\nYour new secure password: {password}\n")

	print(f"{Fore.RED}--- WARNING this message will be deleted in 5 seconds!!! ---{Style.RESET_ALL}")
	time.sleep(5)
	os.system("clear")

	save_password = input(f"{Fore.YELLOW}Do you want save your password into file(y/n): {Style.RESET_ALL}")

	if save_password == 'y':
		with open('password.txt', 'a') as s:
			s.write(f"{stuff_password}: {password}\n")
		print(f"{Fore.GREEN}\nPassword succesfully saved into file!\n{Style.RESET_ALL}")
	else:
		print("Save canceled.")
except ValueError:
	print("Only numbers!")
