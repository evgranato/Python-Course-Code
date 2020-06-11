# ***PYTHON + SQL***

# THERE ARE TONS OF DATABASES OUT THERE AND THEY ARE ALL A BIG PAIN TO INSTALL
# SQLITE3
# - Comes pre-installed on many machines
# - Very simple syntax, not overly complicated or especially powerful
# - SQLITE3 Python module part of Standard Library
# ^d quits sqlite3

# **BASIC SQLITE SYNTAX: CREATE TABLE**
# go to TERMINAL and run sqlite3.
# Make a table by pasting below into TERMINAL:
# CREATE TABLE dogs(name TEXT, breed TEXT, age INTEGER);
# .open dog_db.db will make a new database file.

# **BASIC SQLITE SYNTAX: INSERTING**
# INSERT INTO cats (name, breed, age) VALUES ("Blue", "Scottish Fold", 3);
# Then to see the info: SELECT * FROM cats; returns: Blue|Scottish Fold|3

# CHECK OUT THE FILE: basics.sql
# ENTERED BELOW INTO SQL FILE:
# INSERT INTO dogs (name, age, breed) VALUES("Champ", 4, "Husky");
# INSERT INTO dogs (name, age, breed) VALUES("Rose", 6, "Terrior");
# INSERT INTO dogs (name, age, breed) VALUES("Moose", 5, "Golden");
# INSERT INTO dogs (name, age, breed) VALUES("Jack", 1, "Lab");
# INSERT INTO dogs (name, age, breed) VALUES("Trigger", 9, "Weim");
# INSERT INTO dogs (name, age, breed) VALUES("Old Yeller", 8, "Boxer");

# OPENED SQLITE3, TYPED: sqlite3 dog_db.db
# TYPED: .read basics.sql
# THEN TO VERIFY IT'S IN THERE NOW: SELECT * FROM dogs;

# **BASIC SQLITE SYNTAX: SELECTING**
# SELECT name, age FROM dogs; # gives just the column
# SELECT * FROM dogs WHERE name IS "Moose"; # THIS RETURNS JUST MOOSE'S INFO
# THE sqlite3 DOCS ONLINE HAVE GREAT FLOW CHARTS TO HELP
# SELECT * FROM dogs WHERE name LIKE "%gg%"; # Gives Trigger's info since he has 2 g's.
# RESPONSE: Trigger|Weim|9

# **CONNECTING TO A DB WITH PYTHON**
# FRIENDS:
# import sqlite3
# conn = sqlite3.connect("my_friends.db")
# # LETS CREATE A TABLE:
# # WE USE A CURSOR, WHICH IS A "WORK SPACE"
# # PROCESS:
# # 1. CREATE CURSOR OBJECT
# c = conn.cursor()
# # 2. EXECUTE SOME SQL
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# # 3. COMMIT CHANGES
# conn.commit()
# conn.close()

# **INSERTING WITH PYTHON**
# import sqlite3
# conn = sqlite3.connect("my_friends.db")
# # LETS CREATE A TABLE:
# # WE USE A CURSOR, WHICH IS A "WORK SPACE"
# # PROCESS:
# # 1. CREATE CURSOR OBJECT
# c = conn.cursor()
# # 2. EXECUTE SOME SQL
# # c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# # YOU COULD JUST INSERT LIKE THIS:
# # insert_query = '''INSERT INTO friends
# #                     VALUES ('Merriwether', 'Lewis', 7)'''
# # LETS SAY WE HAVE A CSV OR FORM DATA THAT WE WANT TO GET INTO A DATABASE:
# # HERE'S ONE WAY:
# # form_first = "Dana"
# # query = "INSERT INTO friends (first_name) VALUES (?)"
# # c.execute(query, (form_first,))
# # HERE'S ANOTHER WAY:
# data = ("Steve", "Irwin", 9)
# query = "INSERT INTO friends VALUES (?,?,?)"
# c.execute(query, data)
# # 3. COMMIT CHANGES
# conn.commit()
# conn.close()

# **BULK INSERTS WITH PYTHON**
# import sqlite3
# conn = sqlite3.connect("my_friends.db")
# c = conn.cursor()
#
# people = [
#     ("Roald", "Amundsen", 5),
#     ("Rosa", "Parks", 8),
#     ("Henry", "Hudson", 7),
#     ("Neil", "Armstrong", 7),
#     ("Daniel", "Boone", 3)]
# # COULD DO SOMETHING LIKE THIS:
# # for person in people:
# #     insert that one person
# # BUT THIS IS BETTER:
# # c.executemany("INSERT INTO friends VALUES (?,?,?)", people)
# # AND THIS WILL ALLOW US TO DO ABOVE, BUT PRINT WHAT IT'S DOING:
#
# for person in people:
#     c.execute("INSERT INTO friends VALUES (?,?,?)", person)
#     print("EXECUTING! !")
# conn.commit()
# conn.close()

# **SELECTING USING PYTHON**
# HERE WE WANT THE DATA, NOT JUST APPLY IT.
# import sqlite3
# conn = sqlite3.connect("my_friends.db")
# # CREATE CURSOR OBJECT:
# c = conn.cursor()
# # c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
# # THIS ITERATES ON SEPARATE LINES: TUPLES OF THE INFORMATION:
# # for result in c:
# #     print(result)
# # THIS WILL GIVE US A LIST OF TUPLES:
# #print(c.fetchall())
# # THIS WILL GIVE JUST ONE:
# #print(c.fetchone()) # ('Rosa', 'Parks', 8)
# # LETS SAY WE WANT TO FIND A CERTAIN CLOSENESS AND ORGANIZE BY NUMBER:
# c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
# print(c.fetchall()) # GIVES LIST OF TUPLES OF CLOSENESS >5 ORDERED BY CLOSENESS
# conn.commit()
# conn.close()

# **SQL INJECTION!**
# import sqlite3
# conn = sqlite3.connect("users.db")
# # CREATE CURSOR OBJECT:
#
# u = input("please enter your username...")
# p = input("please enter your password...")
# query = f"SELECT * FROM users WHERE user='{u}' AND password='{p}'"
# c = conn.cursor()
# c.execute(query)
#
# result = c.fetchone()
# if result:
#     print("WELCOME BACK")
# else:
#     print("FAILED LOGIN")
# conn.commit()
# conn.close()
# WE DON'T WANT TO DO THIS BECAUSE YOU CAN ACCESS THE SQL IF YOU INPUT SOMETHING PROPERLY:
# please enter your username...Colt
# please enter your password...' OR 1=1--
# WELCOME BACK
# ******THE ABOVE BREAKS IT BECAUSE YOU ARE ADDING TO THE QUERY LINE.
# IT WOULD CONTINUE BECAUSE (OR 1=1 (THIS IS A TRUE STATEMENT) THE THE -- IS HOW YOU COMMENT
# IN SQL TO CANCEL THE ' OUT AT THE END.) IT CREATES A CONTINUATION OF THE QUERY STRING.

# THIS IS HOW YOU SHOULD DO IT:
# import sqlite3
# conn = sqlite3.connect("users.db")
# # CREATE CURSOR OBJECT:
#
# u = input("please enter your username...")
# p = input("please enter your password...")
# # query = f"SELECT * FROM users WHERE user='{u}' AND password='{p}'"
# query = f"SELECT * FROM users WHERE user=? AND password=?"
# c = conn.cursor()
# c.execute(query,(u,p))
#
# result = c.fetchone()
# if result:
#     print("WELCOME BACK")
# else:
#     print("FAILED LOGIN")
# conn.commit()
# conn.close()

# **SCRAPING TO A DATABASE PT 1**
import sqlite3
import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    save_books(all_books)

def save_books(all_books):
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE books
        (title TEXT, price REAL, rating INTEGER)''')
    c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
    connection.commit()
    connection.close()

def get_title(book):
    return book.find("h3").find("a")["title"]

def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("£", "").replace("Â", ""))

def get_rating(book):
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    paragraph = book.select(".star-rating")[0]
    word = paragraph.get_attribute_list("class")[-1]
    return ratings[word]

scrape_books("http://books.toscrape.com/catalogue/category/books/history_32/index.html")