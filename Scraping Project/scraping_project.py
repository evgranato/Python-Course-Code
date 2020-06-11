# ***QUOTE SCRAPING PROJECT***
# MAKING A GUESSING GAME WHERE SCRAPER GRABS QUOTES FROM A WEBSITE http://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup
# from time import sleep # THIS SPACES OUT REQUESTS TO SITE

site = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(site.text, "html.parser")
org_site = "http://quotes.toscrape.com"
blocks = soup.find_all(class_="quote")
real_all_info = []
for val in blocks:
    real_all_info.append({
        "quotes" : val.find(class_="text").get_text(),
        "authors" : val.find(class_="author").get_text(),
        "url" : org_site + val.find("a")["href"]
    })

count = 1
while blocks:
    pages = soup.find(class_="pager").find("a")["href"][:6:]
    full_next_url = org_site + pages + str(count)
    count += 1
    response = requests.get(str(full_next_url))
    soup = BeautifulSoup(response.text, "html.parser")
    blocks = soup.find_all(class_="quote")

    for val in blocks:
        real_all_info.append({
            "quotes": val.find(class_="text").get_text(),
            "authors": val.find(class_="author").get_text(),
            "url": org_site + val.find("a")["href"]
        })
    #sleep(1) # SLOWS DOWN THE REQUESTS FOR POLITENESS



# site = requests.get("http://quotes.toscrape.com")
# soup = BeautifulSoup(site.text, "html.parser")
# org_site = "http://quotes.toscrape.com"
# blocks = soup.find_all(class_="quote")
# real_all_info = []
# for val in blocks:
#     quote = val.find(class_="text")
#     quotes = quote.get_text()
#     author = val.find(class_="author")
#     authors = author.get_text()
#     author_url = org_site + val.find("a")["href"]
#     all_info = (quotes, authors, author_url)
#     real_all_info += all_info
#
# count = 1
# while blocks:
#     pages = soup.find(class_="pager").find("a")["href"][:6:]
#     full_next_url = org_site + pages + str(count)
#     count += 1
#     response = requests.get(str(full_next_url))
#     soup = BeautifulSoup(response.text, "html.parser")
#     blocks = soup.find_all(class_="quote")
#
#     for val in blocks:
#         quote = val.find(class_="text")
#         quotes = quote.get_text()
#         author = val.find(class_="author")
#         authors = author.get_text()
#         author_url = org_site + val.find("a")["href"]
#         all_info2 = (quotes, authors, author_url)
#         real_all_info += all_info2
# print("Finished")