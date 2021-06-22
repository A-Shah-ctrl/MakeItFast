'''
Author: Ashka Shah
Date: June 22, 2021

Give the URL of a website its extracts text.
The website must not require authentication.
'''

import requests
from bs4 import BeautifulSoup


class Extract():
    #==== Public Methods ====
    def __init__(self, website:str):
        self._fetch_content(website)

    def get_content(self):
        '''
        Returns the text on the website as one string
        '''
        return self._content

    # ==== Private Methods ====
    def _fetch_content(self, website: str):
        raw_text = requests.get(website).text
        parsed_text = BeautifulSoup(raw_text, 'html.parser')
        self._content = self._filter(parsed_text)

    def _filter(self, parsed_text:BeautifulSoup):
        content = ''
        paragraphs = parsed_text.find_all("p")
        for para in paragraphs:
            content += para.text
        return content

# if __name__ == "__main__":
#     e = Extract("https://en.wikipedia.org/wiki/Mariam-uz-Zamani")
#     print(e.content)
