import requests
from bs4 import BeautifulSoup
import json

class ParserCBRF:
    def __init__(self, url, filename="cbrf_data.json"):
        self.url = url
        self.filename = filename
        self.data = {}

    def start(self):
        html = self._get_html()
        if html:
            self._parse(html)
            if self.data:
                self._save()
            else:
                print("Нет данных для сохранения.")
        else:
            print("Не удалось загрузить страницу.")
        print("Парсер завершил работу.")

    def _get_html(self):
        try:
            response = requests.get(self.url, timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print("Ошибка загрузки:", e)
        return None

    def _parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table")
        if not table:
            print("Таблица не найдена.")
            return
        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            if len(cols) >= 2:
                date = cols[0].get_text(strip=True)
                rate = cols[1].get_text(strip=True)
                self.data[date] = rate

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=2)
        print(f"Сохранено {len(self.data)} записей в {self.filename}")

    def _load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.data = json.load(file)
            print(f"Данные загружены из {self.filename}")
        except Exception as e:
            print("Ошибка загрузки:", e)

if __name__ == "__main__":
    parser = ParserCBRF("https://www.cbr.ru/hd_base/keyrate/")
    parser.start()
    # parser._load()