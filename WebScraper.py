import csv
from datetime import datetime
import urllib.request
from bs4 import BeautifulSoup

class WebScraper(object):

    def quote_page(self, page_url):

        page = urllib.request.urlopen(page_url)
        soup = BeautifulSoup(page, 'html.parser')
        name_box = soup.find('h1', attrs={'class': 'name'})

        name = name_box.text.strip()
        print('Name: %s' % name)

        price_box = soup.find('div', attrs={'class':'price'})
        price = price_box.text
        print('Price: %s' % price)

        with open('index.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([name, price, datetime.now()])

    def save_as_csv(self, filename):
         pass
