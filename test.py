from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.avclub.com")
rtext = r.text
soup = BeautifulSoup(rtext, "lxml")
# articles = soup.find('article')
# print articles.prettify()
inners = soup.find_all('h1','heading')
c = 0
for e in inners:
    try:
        c += 1
        print e.a['title'].encode('utf-8')
    except (KeyError, TypeError):
        pass
print "--- Counted {} titles ---".format(c)
