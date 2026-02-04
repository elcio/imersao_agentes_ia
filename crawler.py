import os
import re
import requests
from hashlib import md5
from bs4 import BeautifulSoup


class Crawler:

    def __init__(self, base_url):
        self.base_url = base_url
        self.visited = set()
        self.to_visit = [base_url]
        self.data = []

    def crawl(self):
        while self.to_visit:
            url = self.to_visit.pop()
            if url in self.visited:
                continue
            self.visit(url)
        return self.data

    def visit(self, url):
        print(f'Visiting {url} ({len(self.data)} found, {len(self.to_visit)} left)')
        try:
            url_hash = md5(url.encode('utf-8')).hexdigest()
            if not os.path.exists(f'cache/{url_hash}.html'):
                response = requests.get(url)
                html = response.text
                with open(f'cache/{url_hash}.html', 'w') as f:
                    f.write(html)
            else:
                with open(f'cache/{url_hash}.html', 'r') as f:
                    html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith(self.base_url) and href not in self.visited and href.endswith('/') and '/category/' not in url:
                    self.to_visit.append(href)
            if len(url.split('/')) <= 5:
                self.data.append(self.extract_data(url, soup))
            self.visited.add(url)
        except requests.exceptions.RequestException as e:
            print(f'Failed to visit {url}: {e}')
            self.to_visit.append(url)

    def extract_data(self, url, soup):
        title = soup.title.string if soup.title else 'No title'
        sections = soup.find_all('section')
        text = ' '.join([section.get_text() for section in sections])
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r' +', ' ', text)
        return {
            'url': url,
            'title': title,
            'text': text
        }

if __name__ == '__main__':
    crawler = Crawler('https://visie.com.br')
    data = crawler.crawl()
    print(data[-2:])
