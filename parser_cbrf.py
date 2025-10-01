import requests
from bs4 import BeautifulSoup
import json

class ParserCBRF:
    def __init__(self, url):
        self._url = url
        self._data = {}

    def start(self):
        html = self._get_html()
        self._parse(html)
        self._to_json('data.json')

    def _get_html(self):
        return requests.get(self._url).text

    def _parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) >= 2:
                date = cols[0].text.strip()
                value = cols[1].text.strip()
                self._data[date] = value

    def _to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2)

    def _from_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
