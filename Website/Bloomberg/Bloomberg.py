from ..Website import Website

from bs4 import BeautifulSoup
from datetime import datetime
class Bloomberg(Website):

    def __init__(self):
        super(Bloomberg, self).__init__()
        self.url = 'http://www.bloomberg.com/quote/CCMP:IND'
        self.url = 'http://www.bloomberg.com/quote/SPX:IND'

    def parse_attributes(self, page):
        super(Bloomberg, self).parse_attributes(page)

        soup = BeautifulSoup(page, 'html.parser')

        name_box = soup.find('h1', attrs={'class': 'name'})

        name = name_box.text.strip()

        price_box = soup.find('div', attrs={'class':'price'})
        price = price_box.text

        return [name, price, datetime.now()]
