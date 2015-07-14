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
    r = requests.get("https://hr.hamilton.ca/psc/hr9eapps/EMPLOYEE/HRMS/c/HRS_HRAM.HRS_CE.GBL?PortalActualURL=https%3a%2f%2fhr.hamilton.ca%2fpsc%2fhr9eapps%2fEMPLOYEE%2fHRMS%2fc%2fHRS_HRAM.HRS_CE.GBL&amp;PortalContentURL=https%3a%2f%2fhr.hamilton.ca%2fpsc%2fhr9eapps%2fEMPLOYEE%2fHRMS%2fc%2fHRS_HRAM.HRS_CE.GBL&amp;PortalContentProvider=HRMS&amp;PortalCRefLabel=Careers&amp;PortalRegistryName=EMPLOYEE&amp;PortalServletURI=https%3a%2f%2fhr.hamilton.ca%2fpsp%2fhr9eapps%2f&amp;PortalURI=https%3a%2f%2fhr.hamilton.ca%2fpsc%2fhr9eapps%2f&amp;PortalHostNode=HRMS&amp;NoCrumbs=yes&amp;PortalKeyStruct=yes")
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")

    job_table = soup.find('table', attrs={'id': 'tdgbrHRS_CE_JO_EXT_I$0'})
    rows = job_table.find_all('tr')

    data = []

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        cols.append('https://hr.hamilton.ca/psp/hr9eapps/EMPLOYEE/HRMS/c/HRS_HRAM.HRS_CE.GBL')
        data.append([ele for ele in cols if ele])

    with open('jobs_mississauga.csv', 'wb') as FILE:
        writer = csv.writer(FILE, delimiter=',')
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    parse_toronto()
    parse_hamilton()
