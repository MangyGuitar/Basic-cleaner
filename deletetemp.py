import os
from colorama import Fore, Back, just_fix_windows_console, Style


os.system("title Delete Temp and Trash archives")

print(Fore.CYAN + Style.BRIGHT)
os.system("rd %temp% /s /q")
os.system("rd temp /s /q")
os.system("ipconfig /flushdns")
os.system("wuauclt /detectnow")
os.system("wuauclt /updatenow")
os.system("wuauclt /detectnow /updatenow")

os.system("")
