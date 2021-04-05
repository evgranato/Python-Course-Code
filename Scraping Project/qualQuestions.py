import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictWriter
# from time import sleep # THIS SPACES OUT REQUESTS TO SITE

site = requests.get("https://blog.hubspot.com/sales/16-sales-qualification-questions-to-identify-prospects-worth-pursuing")

def scrape_quotes():
    soup = BeautifulSoup(site.text, "html.parser")
    org_site = "https://blog.hubspot.com/sales/16-sales-qualification-questions-to-identify-prospects-worth-pursuing"
    blocks = soup.find_all(class_="post-body")
    something = soup.find_all("h3")
    real_all_info = []
    i = 0
    # while i < 30:
    #     blocks = soup.find_all(class_="post-body")
    #     for val in blocks:
    #         i += 1
    #         real_all_info.append({
    #             "questions": val.find("h3").get_text()
    #         })
    while i < 30:
        for val in something:
            i += 1
            real_all_info.append({
                "questions": val
            })
    return real_all_info
def write_quotes(questions):
    with open("code/Python Testing/qs2.csv", "w") as file:
        headers = ["questions"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for q in questions:
            csv_writer.writerow(q)

questions = scrape_quotes()
# print(quotes)
write_quotes(questions)