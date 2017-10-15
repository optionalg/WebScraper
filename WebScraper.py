import csv
import urllib.request

from Website.Bloomberg.Bloomberg import Bloomberg

class WebScraper(object):

    def __init__(self):
        self.website = Bloomberg()
        page = self.fetch_page(self.website.url)

        row_data = self.website.parse_attributes(page)
        self.save('index.csv', row_data)

    def fetch_pages(self, page_url_list):
        page_list = []
        for page_url in page_url_list:
            page_list.append(self.fetch_page(page_url))
        return page_list

    def fetch_page(self, page_url):
        return urllib.request.urlopen(page_url)

    def save(self, filename, row_data):
        self.save_as_csv(filename, row_data)

    def save_as_csv(self, filename, row_data):
        with open(filename, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row_data)
