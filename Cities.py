import json

class City(object):
    def __init__(self, name):
        with open("cities.json") as FILE:
            d = json.load(FILE)
            self.request_url = d[name]["request_url"]
            self.soup_find_list = d[name]["soup_find_list"]
            self.csv_name = d[name]["csv_name"]


class Toronto(City):
    def __init__(self):
        City.__init__(self, "toronto")

    def make_csv(self, input_data):
        output_data = []
        first_row = True
        for row in input_data:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if first_row:
                cols.append("Job URL")
                first_row = False
            else:
                url = row.find('a')
                cols.append("https://www.brainhunter.com/frontoffice/" + url['href'].encode('ascii'))
            output_data.append([elem for elem in cols if elem])
        return output_data


class Hamilton(City):
    def __init__(self):
        City.__init__(self, "hamilton")

    def make_csv(self, input_data):
        output_data = []
        for row in input_data:
            cols = row.find_all('td')
            cols = [ele.text.encode('utf-8').strip() for ele in cols]
            cols.append('https://hr.hamilton.ca/psp/hr9eapps/EMPLOYEE/HRMS/c/HRS_HRAM.HRS_CE.GBL')
            output_data.append([elem for elem in cols if elem])
        output_data.insert(0, ["Posting Date", "Job Title", "Job ID", "Department", "Job URL"])
        return output_data


class Mississauga(City):
    def __init__(self):
        City.__init__(self, "mississauga")

    def make_csv(self, input_data):
        output_data = []
        for row in input_data:
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
