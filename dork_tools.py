import requests
from bs4 import BeautifulSoup
import re

class DorkTools:
    @staticmethod
    def google_dork(query, num_results=10):
        url = f"https://www.google.com/search?q={query}&num={num_results}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        results = []
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3', class_='r')
                if title:
                    title = title.text
                    results.append({'title': title, 'link': link})
        
        return results

    @staticmethod
    def file_type_dork(file_type, keyword, num_results=10):
        query = f"filetype:{file_type} {keyword}"
        return DorkTools.google_dork(query, num_results)

    @staticmethod
    def site_dork(site, keyword, num_results=10):
        query = f"site:{site} {keyword}"
        return DorkTools.google_dork(query, num_results)