from pyfiglet import figlet_format
from termcolor import colored
# help(pyfiglet)
def make_ASCII(word, color):
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    val = figlet_format(word)
    color = color.casefold()
    if color in valid_colors:
        art = colored(val, color=color)
        print(art)
    else:
        print("You need to choose another color!")


word = input("What do you want to say?")
color = input("What color?")
make_ASCII(word, color)


