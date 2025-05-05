import csv
import json
import re
print("Поехали")

with open('traders.txt','r') as f:
    INN_list = [line.strip() for line in f if line.strip()]
print("Список ИНН из файла traders.txt:", INN_list)

with open ('traders.json', 'r') as f:
    traders = json.load(f)
    filtered_traders = []
    for t in traders:
        inn = str(t.get('inn', '')).strip()
        if inn in INN_list:
            filtered_traders.append(t)
    if 'inn' in INN_list:
        print(f'Найдено совпадение: {inn}')
print("Найдено организаций:", len(filtered_traders))

with open('traders.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ИНН', 'ОГРН', 'Адрес'])
    for t in filtered_traders:
        writer.writerow([
            t.get('inn', ''),
            t.get('ogrn', ''),
            t.get('address', '')])

def find_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text or "")

emails_by_inn = {}

with open('1000_efrsb_messages.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)

for msg in messages:
    inn = str(msg.get('publisher_inn', '')).strip()
    text = msg.get('msg_text', '')
    emails = find_emails(text)
    if emails:
        if inn not in emails_by_inn:
            emails_by_inn[inn] = set()
        emails_by_inn[inn].update(emails)
emails_by_inn = {k: list(v) for k, v in emails_by_inn.items()}

with open('emails.json', 'w', encoding='utf-8') as f:
    json.dump(emails_by_inn, f, ensure_ascii=False, indent=2)

print("Emails успешно сохранены в emails.json")
