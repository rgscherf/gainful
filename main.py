from bs4 import BeautifulSoup
import requests
import unicodecsv
from itertools import chain

import orgs

organizations = [ orgs.Toronto()
         , orgs.Hamilton()
         , orgs.Mississauga()
         , orgs.Victoria()
         , orgs.CRD()
         , orgs.OPS()
         ]

def parse(org):
    r = requests.get(org.request_url)
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")
    data = org.make_data(soup)
    return data

def main():
    source = []

    for o in organizations:
        source.append(parse(o))

    flattened_list = list(chain.from_iterable(source))

    with open("combined.csv", "wb") as FILE:
        writer = unicodecsv.writer(FILE, delimiter=",", encoding="utf-8")
        for row in flattened_list:
            writer.writerow(row)

if __name__ == '__main__':
    main()
