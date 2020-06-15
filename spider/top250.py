import bs4
import requests


res = requests.get('https://movie.douban.com/top250',params=None)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
targets = soup.find_all("div", class_="hd")
for each in targets:
    print(each.a.span.text)
