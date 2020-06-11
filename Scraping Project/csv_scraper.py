import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictWriter
# from time import sleep # THIS SPACES OUT REQUESTS TO SITE

site = requests.get("http://quotes.toscrape.com")

def scrape_quotes():
    soup = BeautifulSoup(site.text, "html.parser")
    org_site = "http://quotes.toscrape.com"
    blocks = soup.find_all(class_="quote")
    real_all_info = []
    for val in blocks:
        real_all_info.append({
            "quotes": val.find(class_="text").get_text(),
            "authors": val.find(class_="author").get_text(),
            "url": org_site + val.find("a")["href"]
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
    return real_all_info


def write_quotes(quotes):
    with open("quotes.csv", "w") as file:
        headers = ["quotes", "authors", "url"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)