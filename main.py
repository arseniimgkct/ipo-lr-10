import requests
from bs4 import BeautifulSoup

r = requests.get('https://github.com/trending')
soup = BeautifulSoup(r.text, "html.parser")

rows = soup.find_all('article')

for i in range(0, len(rows)):
    row = rows[i]
    repo = row.find('h2').getText(separator=" ", strip=True)
    
    stars_div = row.find("div", class_="f6 color-fg-muted mt-2")
    stars = stars_div.find("a").getText(strip=True)
    
    print(f'{i+1}. Repository: {repo}; Stars: {stars}')
