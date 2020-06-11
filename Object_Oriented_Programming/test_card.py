from card_deck import Cards
from pyfiglet import figlet_format
from termcolor import colored

ascii_art = figlet_format("CASINO: POKER")
colored_ascii = colored(ascii_art, color="blue")
print(colored_ascii)

d = Deck()
d.shuffle()
print(d)
input("How Many Cards?")