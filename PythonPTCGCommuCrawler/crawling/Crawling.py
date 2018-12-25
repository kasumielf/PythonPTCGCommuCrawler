import requests
from bs4 import BeautifulSoup
from models.Article import Article

def collect(url):
    results = []

    response = requests.get(url)

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    tables = soup.select("div.article-board")

    for tr in tables[1].select("tr"):
        article = split(tr)

        if article is not None:
            results.append(article)

    return results

def split(tr):
    article = tr.select("td.td_article")

    if len(article) > 0 :
        a = Article()

        number = article[0].select("div.inner_number")[0].text.strip()
        title = article[0].select("a.article")[0].text.replace(" ", "").replace("\n", "")
        name = tr.select("td.p-nick")[0].text
        date = tr.select("td.td_date")[0].text.strip()

        a.setData(number, title, date, name)
        
        return a
    else:
        return None