from pyfiglet import figlet_format
from termcolor import colored

ascii_art = figlet_format("DAD JOKE 3000")
colored_ascii = colored(ascii_art, color="blue")
print(colored_ascii)
# term = input("What subject of joke would you like to hear?")

import requests
url = "https://icanhazdadjoke.com/search"
user_input = input("What subject of joke would you like to hear? ")
number_jokes = input("How many jokes do you want to hear? ")
res = requests.get(
    url,
    headers={"Accept" : "application/json"},
    params={"term" : user_input, "limit" : number_jokes}
)# or .json()

data = res.json()

# print(type(data)) # dictionary
# print(f"I've got {data['total_jokes']} about {user_input} and here is one: ")
num_jokes = data["total_jokes"]

if num_jokes > 1:
    print(f"There are {num_jokes} jokes!")
elif num_jokes == 1:
    print("There is one joke")
    print(data['results'][0]['joke'])
else:
    print(f"Sorry, couldn't find a joke with your term: {user_input}")
    user_input = input("What subject of joke would you like to hear? ")
