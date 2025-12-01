import requests, json
from bs4 import BeautifulSoup

class Repository:
    def __init__(self, name, stars):
        self.name = name
        self.stars = stars
    
    def to_dict(self):
        return {
            "name": self.name,
            "stars": self.stars
        }

r = requests.get('https://github.com/trending')
soup = BeautifulSoup(r.text, "html.parser")

rows = soup.find_all('article')

repos = []
print("Парсим репозитории...")
for i in range(0, len(rows)):
    row = rows[i]
    repo = row.find('h2').getText(separator=" ", strip=True)
    
    stars_div = row.find("div", class_="f6 color-fg-muted mt-2")
    stars = stars_div.find("a").getText(strip=True)
    
    repository = Repository(repo, stars)
    repos.append(repository.to_dict())
    
with open("repositories.json", "w+", encoding="utf-8") as f:
    json.dump(repos, f, indent=2)
    print("Репозитории в repositories.json успешно записаны")