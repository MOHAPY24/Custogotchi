import inspect
import os
import time


def debug(msg):
    print(f"[{inspect.stack()[1].function}]{msg}")

def colour_text(text, colour_code):
    return f"\033[1;{colour_code}m{text} \033[0m" # 91 = red, 92 = green, 93 = yellow, 64 = blue, 95 = magenta, 96 = cyan, 1 = bold, 4 = underline

def cleancnsl():
    if os.name == 'nt':
      os.system("cls")
    else:
      os.system("clear")

