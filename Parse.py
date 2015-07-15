from bs4 import BeautifulSoup
import requests
import unicodecsv

import Orgs

def parse(org):
    r = requests.get(org.request_url)
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")

    data = org.make_data(soup)

    with open(org.csv_name, "wb") as FILE:
        writer = unicodecsv.writer(FILE, delimiter=",", encoding="utf-8")
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    # cities = [ Orgs.Toronto()
    #          , Orgs.Mississauga()
    #          , Orgs.Hamilton()
    #          , Orgs.Victoria()
    #          , Orgs.CRD()
    #          , Orgs.OPS()
    #          ]

    cities = [Orgs.Toronto()]
    for c in cities:
        parse(c)
