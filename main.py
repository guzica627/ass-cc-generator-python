import random
import string
import os
import ctypes
import time
from colorama import Fore

months = ["01","02","03","04","05","06","07","08","09","10","11","12"]

os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("Modcl CC")
print(Fore.LIGHTYELLOW_EX+"""

███╗   ███╗ ██████╗ ██████╗  ██████╗██╗     
████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║     
██╔████╔██║██║   ██║██║  ██║██║     ██║     
██║╚██╔╝██║██║   ██║██║  ██║██║     ██║     
██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╗███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝╚══════╝

         Made by ~ [guzica627]                                                                                                                                     
""")

amount = int(input(Fore.WHITE+"("+Fore.LIGHTYELLOW_EX+"/"+Fore.WHITE+")"+Fore.LIGHTYELLOW_EX+" How much credit cards to generate \n>"))
print()
lenght = int(input(Fore.WHITE+"("+Fore.LIGHTYELLOW_EX+"/"+Fore.WHITE+")"+Fore.LIGHTYELLOW_EX+" What's the lenght of card you want to generate \n>"))

value = 1
while value <= amount:

    number = ('').join(random.choices(string.digits, k=lenght))
    cvv = ('').join(random.choices(string.digits, k=3))
    year = "202" + ('').join(random.choices(string.digits, k=1))
    month = random.choice(months)
    cc = number + "|" + month + "|" + year + "|" + cvv
    value += 1

    print(f"{cc}")
    f = open("output.txt", "a+")
    f.write(f"{cc}\n")
    f.close()

print()
print(Fore.WHITE+"("+Fore.LIGHTYELLOW_EX+"/"+Fore.WHITE+")"+Fore.LIGHTYELLOW_EX+" Done! Results are saved in output.txt , program will close in 5 seconds...")
time.sleep(5)
