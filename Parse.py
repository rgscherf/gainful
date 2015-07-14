from bs4 import BeautifulSoup
import requests
import csv

import Cities


def parse(city):
    r = requests.get(city.request_url)
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")

    job_table = soup.find( city.soup_find_list[0] ,
                           city.soup_find_list[1] )
    rows = job_table.find_all("tr")
    data = city.make_csv(rows)

    with open(city.csv_name, "wb") as FILE:
        writer = csv.writer(FILE, delimiter=",")
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    cities = [ Cities.Toronto()
             , Cities.Hamilton() ]

    for c in cities:
        parse(c)
