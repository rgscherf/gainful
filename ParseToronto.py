from bs4 import BeautifulSoup
import requests
import csv

# parsing HTML table with BeautifulSoup: http://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table

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

with open('toronto_jobs.csv', 'wb') as FILE:
    writer = csv.writer(FILE, delimiter=',')
    for row in data:
        writer.writerow(row)
