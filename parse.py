from bs4 import BeautifulSoup
from itertools import chain
import requests
import orgs

organizations = [ orgs.Toronto()
         , orgs.Hamilton()
         , orgs.Mississauga()
         , orgs.Victoria()
         , orgs.CRD()
         , orgs.OPS()
         ]

# organizations = [ orgs.Toronto() ]

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

    return flattened_list
