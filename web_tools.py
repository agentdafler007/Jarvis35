import requests
from bs4 import BeautifulSoup

class WebTools:
    @staticmethod
    def fetch_webpage_content(url):
        response = requests.get(url)
        return response.text

    @staticmethod
    def extract_links(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links

    @staticmethod
    def extract_text(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text()