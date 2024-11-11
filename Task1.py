import requests
from bs4 import BeautifulSoup

url = 'https://edition.cnn.com'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

for i in range(1, 7):  # Перебір заголовків від h1 до h6
    headers = soup.find_all(f'h{i}')
    for header in headers:
        print(f'Тег h{i}: {header.get_text(strip=True)}')

links = soup.find_all('a')
for link in links:
    url = link.get('href')
    content = link.get_text(strip=True)
    print(f'Посилання URL: {url}, Вміст: {content}')

images = soup.find_all('img')
print(f'Кількість зображень: {len(images)}')
for img in images:
    alt_text = img.get('alt', 'Немає alt')
    print(f'Значення alt: {alt_text}')
