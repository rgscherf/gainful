from bs4 import BeautifulSoup
import requests
from itertools import chain
import orgs


# import unicodecsv

# organizations = [ orgs.Toronto()
#          , orgs.Hamilton()
#          , orgs.Mississauga()
#          , orgs.Victoria()
#          , orgs.CRD()
#          , orgs.OPS()
#          ]

organizations = [ orgs.Toronto() ]

def parse(org):
    r = requests.get(org.request_url)
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")
    data = org.make_data(soup)
    return data

def build_parse_list():
    source = []

    for o in organizations:
        source.append(parse(o))

    flattened_list = list(chain.from_iterable(source))
    for i in flattened_list:
        for j in i:
            j.encode('utf-8')

    return flattened_list

    # with open("combined.csv", "wb") as FILE:
    #     writer = unicodecsv.writer(FILE, delimiter=",", encoding="utf-8")
    #     for row in flattened_list:
    #         writer.writerow(row)
