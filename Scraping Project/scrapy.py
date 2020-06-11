# ***SCRAPY***
# BUILD AND RUN YOUR OWN WEB SPIDERS
# FRAMEWORK FOR SCRAPING DATA
# MAKING A BOOK SCRAPER:
# http://books.toscrape.com

import scrapy


class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css(".price_color::text").extract_first()
            }

# TO RUN SCRAPY, IN TERMINAL: scrapy runspider -o books.csv scrapy.py
# SCRAPY RUNSPIDER -O "FILE TO WRITE TO" "PYTHON FILE WITH CODE"
