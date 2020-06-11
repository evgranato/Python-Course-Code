# ***CODE ALONG PROJECT***
# ASCII Art Exercise

from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color):
    blink_on = []
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

    if color not in valid_colors:
        color = "magenta"
    if blink == "y":
        blink_on = ["blink"]
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color, attrs=blink_on)
    print(colored_ascii)

msg = input("What would you like to print?")
color = input("What color?")
blink = input("Blink? y or n: ")
print_art(msg, color)
