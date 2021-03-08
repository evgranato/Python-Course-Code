# ***WEB SCRAPING***
# OBJECTIVES:
# - Define what web scraping is and the issues surrounding it
# - Use the requests and BeautifulSoup modules to parse HTML
# - Explain some common problems with web scraping
# - Explore other tools that can interact with web pages

# **INTRODUCING WEB SCRAPING**
# - Web scraping involves programatically grabbing data from a web page
# - Three steps: Download, extract data, PROFIT!!

# WHY SCRAPE?
# - There's data on a site that you want to store or analyze
# - You can't get by other means (e.g. and API)
# - You want to programmatically grab the data (instead of lots of manual copying/pasting)

# **IS SCRAPING OK?**
# - Some websites don't want people scraping them
# - Best practice: consult the robots.txt file
# - If making many requests, time them out
# - If you're too aggressive, your IP can be blocked

# **HTML AND CSS CRASH COURSE**
# CHECK OUT HTML_Crash_Course.html FILE TO SEE THE EXAMPLE WE CREATED

# **INTRODUCTION TO BEAUTIFUL SOUP**
# download module bs4
# - To extract data from HTML, we'll use Beautiful Soup
# - Install it with pip
# - Beautiful Soup lets us navigate through HTML with Python
# - Beautiful Soup does NOT download HTML - for this, we need the requests module!

# html= """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>First HTML Page</title>
# </head>
# <body>
#     <div id="first">
#       <h3 data-example="yes">hi</h3>
#       <p>more test.</p>
#     </div>
#     <ol>
#       <li class="special">This list item is special.</li>
#       <li class="special">This list item is also special.</li>
#     </ol>
#     <div>bye</div>
# </body>
# </html>
# """

# PARSING AND NAVIGATING HTML:
# - BeautifulSoup(html_string, "html.parser") - parse HTML
# - Once parsed, There are several ways to navigate:
#       - By Tag Name
#       - Using find - returns one matching tag
#       - Using find_all - returns a list of matching tags

# NAVIGATING WITH CSS SELECTORS:
# - select - returns a list of elements matching a CSS selector

# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(html, "html.parser")
# print(soup)
# print(type(soup)) # <class 'bs4.BeautifulSoup'>
# print(soup.body.div) # WE ONLY GOT THE FIRST DIV
# var = soup.find("div")
# print(type(var)) # <class 'bs4.element.Tag'>
# THE ABOVE IS IT'S OWN OBJECT
# d = soup.find_all("div")
# print(d) # RETURNS A LIST:
# [<div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more test.</p>
# </div>, <div>bye</div>]
# d = soup.find(id="first") # WE ARE SEARCHING BY ID
# print(d)
# d = soup.find_all(class_="special") # ******IMPORTANT: YOU MUST USE class_ INSTEAD OF JUST CLASS******
# print(d) # RETURNS CLASS
# d = soup.find_all(attrs={"data-example" : "yes"})
# print(d) # RETURNS THE ATTRIBUTE YOU SEARCH

# CSS STYLE SELECTORS:
# select - returns a list of elements matching a CSS selector
# CHEAT SHEET:
#       - Select by id of foo: #foo
#       - Select by class of bar: .bar
#       - Select Children: div > p
#       - Select descendents: div p
# ***HTML CODE IS ABOVE***
# from bs4 import BeautifulSoup

# soup = BeautifulSoup(html, "html.parser")
# d = soup.select("#first") # WE GET A LIST USING .select SELECTING FOR ID
# print(d) # RETURNS:
# [<div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more test.</p>
# </div>]
# d = soup.select(".special") # SELECTING FOR CLASS
# print(d) # RETURNS:
# [<li class="special">This list item is special.</li>, <li class="special">This list item is also special.</li>]
# d = soup.select("div") # SELECTING FOR TAG NAME (DIV)
# print(d)
# d = soup.select("[data-example]") # SELECTING FOR ATTRIBUTE
# print(d)

# YOU CAN USE FIND/FIND ALL OR SELECT:
# - SELECT ALWAYS RETURNS A LIST.
# - ONLY FIND ALL RETURNS A LIST.

# **ACCESSING DATA USING BEAUTIFUL SOUP**
# - get_text - access the inner text in an element
# - name - tag name
# - attrs - dictionary of attributes
# - You can also access attribute values using brackets

# html = """
#  <!DOCTYPE html>
#  <html lang="en">
#  <head>
#      <meta charset="UTF-8">
#      <title>First HTML Page</title>
#  </head>
#  <body>
#      <div id="first">
#        <h3 data-example="yes">hi</h3>
#        <p>more test.</p>
#      </div>
#      <ol>
#        <li class="special">This list item is special.</li>
#        <li class="special">This list item is also special.</li>
#      </ol>
#      <div>bye</div>
#  </body>
#  </html>
#  """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")
# el = soup.select(".special")[0] # EL IS FOR ELEMENT
# # print(el.get_text()) # This list item is special.
# # print(el) # <li class="special">This list item is special.</li>
# # for el in soup.select(".special"):
# #     print(el.get_text())
# # ITERATES AND RETURNS ALL OF THE ELEMENTS THAT MATCH THE CLASS:
# # This list item is special.
# # This list item is also special.
# # for el in soup.select(".special"):
# #     print(el.name) # li
# #     print(el.attrs) # {'class': ['special']}
# attr = soup.find("h3")["data-example"]
# print(attr) # yes

# ***NAVIGATING WITH BEAUTIFUL SOUP***
# MOVING AROUND THE HTML RELATIVE TO THE TAG YOU CHOOSE
# VIA TAGS:
# - parent / parents
# - contents
# - next_sibling / next_siblings
# - previous_sibling / previous_siblings
# VIA SEARCHING:
# - find_parent / find_parents
# - find_next_sibling / find_next_siblings
# - find_previous_sibling / find_previous_siblings

# html = """
#  <!DOCTYPE html>
#  <html lang="en">
#  <head>
#      <meta charset="UTF-8">
#      <title>First HTML Page</title>
#  </head>
#  <body>
#      <div id="first">
#        <h3 data-example="yes">hi</h3>
#        <p>more text.</p>
#      </div>
#      <ol>
#        <li class="special super-special">This list item is special.</li>
#        <li>This list item is not special.</li>
#        <li class="special">This list item is also special.</li>
#      </ol>
#      <div>bye</div>
#  </body>
#  </html>
#  """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")
# #data = soup.body.contents[1].next_sibling.next_sibling
# # print(data) # WE GET A LIST OF THE CONTENTS OF THE BODY WITH ALL THE \n "NEW LINE" CHARACTERS
# # data = soup.find(class_="super-special").parent.parent
# # print(data)
#
# # data = soup.find(id="first").find_next_sibling() # SKIPS EMPTY ELEMENTS***
# # data = soup.find(id="first").find_next_sibling().find_next_sibling() # <div>bye</div>
# # print(data)
# # data = soup.find(class_="super-special").find_next_sibling(class_="special")
# # print(data) # <li class="special">This list item is also special.</li>
# # data = soup.find("h3").find_parent()
# data = soup.find("h3").find_parent("html")
# print(data)

# ***OUR FIRST SCRAPING PROGRAM!***
# REQUESTS + BEAUTIFUL SOUP EXAMPLE:
# - Let's scrape data into a CSV!
# - Goal: Grab all links from Rithm School Blog
# - Data: store URL, anchor tag and date

# https://www.rithmschool.com/blog
# import requests
# from bs4 import BeautifulSoup
# from csv import writer
#
# response = requests.get("https://www.rithmschool.com/blog")
# soup = BeautifulSoup(response.text, "html.parser")
# articles = soup.find_all("article")
#
# with open("blog_data.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["title", "link", "date"])
#
#     for article in articles:
#         a_tag = article.find("a")
#         title = a_tag.get_text()
#         url = a_tag["href"]
#         date = article.find("time")["datetime"]
#         csv_writer.writerow([title,url,date])

# ON YOUR OWN, CREATE A WEB CRAWLER THAT GOES TO THE NEXT PAGE UNTIL IT RUNS OUT:

# import requests
# from bs4 import BeautifulSoup
# from csv import writer

# response = requests.get("https://www.rithmschool.com/blog")
# soup = BeautifulSoup(response.text, "html.parser")
# articles = soup.find_all("article")

# with open("blog_data.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["title", "link", "date"])

#     for article in articles:
#         a_tag = article.find("a")
#         title = a_tag.get_text()
#         url = "https://www.rithmschool.com" + a_tag["href"]
#         date = article.find("time")["datetime"]
#         csv_writer.writerow([title,url,date])

#     pages = soup.find_all(class_="pagination")
#     count = 1
#     while articles:
#         for nav in pages:
#             next_page = nav.find("a")["href"][:11:]
#             full_next_url = "https://www.rithmschool.com" + next_page + str(count)
#             count += 1


#             response = requests.get(str(full_next_url))
#             soup = BeautifulSoup(response.text, "html.parser")
#             articles = soup.find_all("article")

#             for article in articles:
#                 a_tag = article.find("a")
#                 title = a_tag.get_text()
#                 url = "https://www.rithmschool.com" + a_tag["href"]
#                 date = article.find("time")["datetime"]
#                 csv_writer.writerow([title, url, date])
#     print("Finished")

nums = [1,2,3,4]

for num in nums:
    print(num)