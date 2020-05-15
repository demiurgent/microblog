import requests
import pprint
from bs4 import BeautifulSoup


def corona_news():

    page = requests.get("https://korrespondent.net")
    soup = BeautifulSoup(page.content, 'html.parser')
    markers=("коронавирус", "-19", "SARS")
    results = soup.find_all("div",
                        string=lambda text: True if (text is not None and any(m in text.lower() for m in markers)) else False)
    articles = {}
    for r in results:
        key = r.find("a")["href"]
        raw_value = r.parent.find("div", class_="article__time")
        value = raw_value.text if raw_value is not None else "NA"
        articles[key] = value

    return articles

print(corona_news())