from bs4 import BeautifulSoup
import requests
import csv

def parse_toronto():
    r = requests.get("https://www.brainhunter.com/frontoffice/searchSeekerJobAction.do?sitecode=pl389&locationPicker=Y&jobStream=&locationId=&levelIds=6&levelContent6=&keyword=&search=Search&order=&sortField=&goJobDetail=&sortedit=&externaljob=#searchSection")
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")

    job_table = soup.find('table', attrs={'class': "job_list_table"})
    rows = job_table.find_all('tr')

    data = []
    firstRow = True

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if firstRow:
            cols.append("Job URL")
            firstRow = False
        else:
            url = row.find('a')
            cols.append("https://www.brainhunter.com/frontoffice/" + url['href'].encode('ascii'))
        data.append([ele for ele in cols if ele])

    with open('jobs_toronto.csv', 'wb') as FILE:
        writer = csv.writer(FILE, delimiter=',')
        for row in data:
            writer.writerow(row)

def parse_hamilton():
    r = requests.get("https://hr.hamilton.ca/psp/hr9eapps/EMPLOYEE/HRMS/c/HRS_HRAM.HRS_CE.GBL")
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")

    job_table = soup.find_all('table', attrs={'id': 'divgbrHRS_CE_JO_EXT_I$0'})
    print job_table
    #job_table = job_table.tbody
    rows = job_table.find_all('tr')

    data = []
    # data.append(["Job ID", "Job Title", "Location", "Posting Date", "Job URL"])

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        url = row.find('a')
        cols.append(url['href'].encode('ascii'))
        data.append([ele for ele in cols if ele])

    with open('jobs_mississauga.csv', 'wb') as FILE:
        writer = csv.writer(FILE, delimiter=',')
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    # parse_toronto()
    parse_hamilton()
