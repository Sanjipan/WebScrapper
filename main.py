import sys
from WebScrapperLib import WebScrapper
if __name__ == '__main__':

    # for test
    WebScrapper.parser('https://quotes.toscrape.com', headers={'user-agent': 'tiny scraper'})