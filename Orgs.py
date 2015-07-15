import json

def log(elem):
    with open("log.html", "wb") as FILE:
        FILE.write(elem)

class Organization(object):
    def __init__(self, name):
        with open("Orgs.json") as FILE:
            d = json.load(FILE)
            self.request_url = d[name]["request_url"]
            self.soup_find_list = d[name]["soup_find_list"]
            self.csv_name = d[name]["csv_name"]


class Toronto(Organization):
    def __init__(self):
        Organization.__init__(self, "toronto")

    def make_data(self, input_data):
        job_table = input_data.find(self.soup_find_list[0], self.soup_find_list[1])
        rows = job_table.find_all('tr')

        output_data = []
        first_row = True

        for row in rows:
            cols = row.find_all('td')
            cols = [elem.text.strip() for elem in cols]
            if first_row:
                cols.append("Job URL")
                first_row = False
            else:
                url = row.find('a')
                cols.append("https://www.brainhunter.com/frontoffice/" + url['href'].encode('ascii'))
            output_data.append([elem for elem in cols if elem])

        del output_data[0]
        output_data.insert(0, ["Posting Date", "Job Title", "Division", "Job Type", "Job Location", "Job URL"])
        return output_data


class Hamilton(Organization):
    def __init__(self):
        Organization.__init__(self, "hamilton")

    def make_data(self, input_data):
        output_data = []
        job_table = input_data.find(self.soup_find_list[0], self.soup_find_list[1])
        rows = job_table.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols = [elem.text.encode('utf-8').strip() for elem in cols]
            cols.append('https://hr.hamilton.ca/psp/hr9eapps/EMPLOYEE/HRMS/c/HRS_HRAM.HRS_CE.GBL')
            output_data.append([elem for elem in cols if elem])

        output_data.insert(0, ["Posting Date", "Job Title", "Job ID", "Department", "Job URL"])

        return output_data


class Mississauga(Organization):
    def __init__(self):
        Organization.__init__(self, "mississauga")

    def make_data(self, input_data):
        output_data = []
        job_table = input_data.find(self.soup_find_list[0], self.soup_find_list[1])
        rows = job_table.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols_clean = []
            for elem in cols:
                elem.span.decompose()
                elem = elem.text.strip()
                cols_clean.append(elem)
            output_data.append([elem for elem in cols_clean if elem])

        del output_data[0]
        output_data.insert(0, ["Job ID", "Job Title", "Job Location", "Posted Date", "Job URL"])

        return output_data


class Victoria(Organization):
    def __init__(self):
        Organization.__init__(self, "victoria")

    def make_data(self, input_data):
        output_data = []
        job_table = input_data.find(self.soup_find_list[0], self.soup_find_list[1])
        rows = job_table.find_all('tr')
        rows = input_data[1:]

        for row in rows:
            cols = row.find_all('td')
            cols = [elem.text.strip() for elem in cols]
            urls = row.find_all('a')
            url = ('http://www.victoria.ca' + urls[1]['href']).encode('ascii')
            cols.append(url)
            output_data.append([elem for elem in cols if elem])

        output_data.insert(0, ["Job Title", "Job ID", "Department", "Status", "Closing Date", "Apply", "Details", "Job URL"])
        for elem in output_data:
            del elem[6]
            del elem[5]
            del elem[3]

        return output_data


class CRD(Organization):
    def __init__(self):
        Organization.__init__(self, "crd")

    def make_data(self, input_data):
        output_data = []
        job_table = input_data.find(self.soup_find_list[0], self.soup_find_list[1])
        rows = job_table.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols = [elem.text.strip() for elem in cols]
            url = row.find('a')
            if url:
                cols.append("http://www.crd.bc.ca" + url['href'].encode('utf-8'))
            output_data.append([elem for elem in cols if elem])

        del output_data[0]
        for elem in output_data:
            del elem[2]
        output_data.insert(0, ["Job Title", "Closing Date", "Job URL"])

        return output_data


class OPS(Organization):
    def __init__(self):
        Organization.__init__(self,"ops")

    def make_data(self, input_data):
        job_table = input_data.find(self.soup_find_list[0], self.soup_find_list[1])
        job_table = job_table.parent.table

        rows = job_table.find_all('a')

        output_data = []

        for row in rows:
            finished_row = []
            title = row.text.encode('utf-8').strip()
            finished_row.append(title)
            finished_row.append("https://www.gojobs.gov.on.ca/" + row['href'].encode('utf-8'))

            cols = row.parent.table
            cols = cols.find_all('span')

            odd = False
            for col in cols:
                if not odd:
                    odd = not odd
                    continue
                odd = not odd
                cleaned_string = col.text.encode('utf-8').strip()
                finished_row.append(cleaned_string)
            output_data.append(finished_row)

        output_data.insert(0, ["Job Title", "Job URL", "Ministry", "Salary Range", "Location", "Closing Date"])
        return output_data
