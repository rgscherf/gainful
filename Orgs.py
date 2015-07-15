import json
import dateutil.parser as dp


################################################################################
# OUTPUT FORMAT
# ["Organization", "Job Title", "Division/Ministry", "Posting Date", "URL"]
################################################################################

def log(t):
    t = t.prettify().encode('utf-8')
    with open("log.html", "wb") as FILE:
        FILE.write(t)



class Organization(object):
    def __init__(self, name):
        with open("orgs.json") as FILE:
            d = json.load(FILE)
            self.request_url = d[name]["request_url"]
            self.soup_find_list = d[name]["soup_find_list"]
            self.csv_name = d[name]["csv_name"]
            self.name = d[name]["name"]

    def parse_date(self, date_string):
        date = dp.parse(date_string)
        res = str(date.year) + "/" + str(date.month) + "/" + str(date.day)
        return res

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
        # output_data.insert(0, ["Posting Date", "Job Title", "Division", "Job Type", "Job Location", "Job URL"])

        sorted_output = []
        for elem in output_data:
            sorted_elem = []
            sorted_elem.append(self.name)
            sorted_elem.append(elem[1])
            sorted_elem.append(elem[2])
            sorted_elem.append(self.parse_date(elem[0])) # post date
            sorted_elem.append(elem[5])
            sorted_output.append(sorted_elem)
        return sorted_output


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

        # output_data.insert(0, ["Posting Date", "Job Title", "Job ID", "Department", "Job URL"])

        sorted_output = []
        for elem in output_data:
            sorted_elem = []
            sorted_elem.append(self.name)
            sorted_elem.append(elem[1])
            sorted_elem.append(elem[3])
            sorted_elem.append(self.parse_date(elem[0])) # post date
            sorted_elem.append(elem[4])
            sorted_output.append(sorted_elem)
        return sorted_output


class Mississauga(Organization):
    def __init__(self):
        Organization.__init__(self, "mississauga")

    def make_data(self, input_data):
        output_data = []
        job_table = input_data.find(self.soup_find_list[0], self.soup_find_list[1])
        rows = job_table.find_all('tr')

        first_row = True
        for row in rows:
            row_data = []

            if first_row:
                first_row = not first_row
                continue

            date = row.find('td', 'iCIMS_JobsTableField_4').find_all('span')
            date = date[1].text.encode('utf-8').strip()
            title = row.find('a').text.encode('utf-8').strip()
            title = " ".join([word.capitalize() for word in title.split()])
            url = row.find('a')['href'].encode('utf-8')

            row_data.append(self.name)
            row_data.append(title)
            row_data.append("City of Mississauga")
            row_data.append(self.parse_date(date))
            row_data.append(url)

            output_data.append(row_data)

        return output_data

class Victoria(Organization):
    def __init__(self):
        Organization.__init__(self, "victoria")

    def make_data(self, input_data):
        output_data = []
        job_table = input_data.find(self.soup_find_list[0], self.soup_find_list[1])
        rows = job_table.find_all('tr')
        rows = rows[1:]

        for row in rows:
            cols = row.find_all('td')
            cols = [elem.text.strip() for elem in cols]
            urls = row.find_all('a')
            url = ('http://www.victoria.ca' + urls[1]['href']).encode('ascii')
            cols.append(url)
            output_data.append([elem for elem in cols if elem])

        # output_data.insert(0, ["Job Title", "Job ID", "Department", "Status", "Closing Date", "Apply", "Details", "Job URL"])

        sorted_output = []
        for elem in output_data:
            sorted_elem = []
            sorted_elem.append(self.name)
            sorted_elem.append(elem[0])
            sorted_elem.append(elem[2])
            sorted_elem.append("Closing: " + self.parse_date(elem[4])) # close date
            sorted_elem.append(elem[7])
            sorted_output.append(sorted_elem)
        return sorted_output


class CRD(Organization):
    def __init__(self):
        Organization.__init__(self, "crd")

    def make_data(self, input_data):
        output_data = []
        job_table = input_data.find(self.soup_find_list[0], self.soup_find_list[1])
        job_table = job_table.find('table')
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
        # output_data.insert(0, ["Job Title", "Closing Date", "Job URL"])

        sorted_output = []
        for elem in output_data:
            sorted_elem = []
            sorted_elem.append(self.name)
            sorted_elem.append(elem[0])
            sorted_elem.append("Capital Regional District")
            sorted_elem.append("Closing: " + self.parse_date(elem[1])) # close date
            sorted_elem.append(elem[2])
            sorted_output.append(sorted_elem)
        return sorted_output


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

        # output_data.insert(0, ["Job Title", "Job URL", "Ministry", "Salary Range", "Location", "Closing Date"])

        sorted_output = []
        for elem in output_data:
            sorted_elem = []
            sorted_elem.append(self.name)
            title = " ".join([word.capitalize() for word in elem[0].split()])
            sorted_elem.append(title)
            sorted_elem.append(elem[2])
            sorted_elem.append("Closing: " + self.parse_date(elem[5])) # close date
            sorted_elem.append(elem[1])
            sorted_output.append(sorted_elem)
        return sorted_output
