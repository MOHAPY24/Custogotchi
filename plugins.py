import inspect
import os
import time
from colorama import init, Fore, Back, Style

init()

def printdy(text):
	for i in text:
		if i.isdigit():
			print(Fore.RED + Style.BRIGHT + i, end='', flush=True)
		else:
			print(Style.RESET_ALL, end='', flush=True)
			print(Fore.WHITE + i, end='', flush=True)
		time.sleep(0.054)
	print("")
	return None


def debug(msg):
    print(f"[{inspect.stack()[1].function}]{msg}")

def colour_text(text, colour_code):
    return f"\033[1;{colour_code}m{text} \033[0m" # 91 = red, 92 = green, 93 = yellow, 64 = blue, 95 = magenta, 96 = cyan, 1 = bold, 4 = underline

def cleancnsl():
    if os.name == 'nt':
      os.system("cls")
    else:
      os.system("clear")

