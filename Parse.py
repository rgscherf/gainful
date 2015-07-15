from bs4 import BeautifulSoup
import requests
import unicodecsv
from itertools import chain

import orgs

def parse(org):
    r = requests.get(org.request_url)
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")
    data = org.make_data(soup)
    return data

if __name__ == '__main__':
    # cities = [ orgs.Toronto()
    #          , orgs.Hamilton()
    #          , orgs.Mississauga
    #          , orgs.Victoria()
    #          , orgs.CRD()
    #          , orgs.OPS()
    #          ]

    cities = [ orgs.Mississauga() ]
    source = []
    for c in cities:
        org_data = parse(c)
        source.append(org_data)

    flattened_list = list(chain.from_iterable(source))

    with open("combined.csv", "wb") as FILE:
        writer = unicodecsv.writer(FILE, delimiter=",", encoding="utf-8")
        for row in flattened_list:
            writer.writerow(row)
