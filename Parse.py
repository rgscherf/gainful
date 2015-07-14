from bs4 import BeautifulSoup
import requests
import unicodecsv

import Orgs

def parse(city):
    r = requests.get(city.request_url)
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")

    job_table = soup.find( city.soup_find_list[0] ,
                           city.soup_find_list[1] )
    rows = job_table.find_all('tr')
    data = city.make_csv(rows)

    with open(city.csv_name, "wb") as FILE:
        writer = unicodecsv.writer(FILE, delimiter=",", encoding="utf-8")
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    cities = [ Orgs.Toronto()
             , Orgs.Mississauga()
             , Orgs.Hamilton()
             ]

    for c in cities:
        parse(c)
