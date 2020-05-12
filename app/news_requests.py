import requests
import pprint
from bs4 import BeautifulSoup

page = requests.get("https://korrespondent.net")

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all("a",
                        string=lambda text: "COVID" in text.lower() if text is not None else False)

print(results[0:2])