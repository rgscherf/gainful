import requests
from bs4 import BeautifulSoup
import sys
import orgs
import parse

reload(sys)
sys.setdefaultencoding('utf8')


def determine_bounds():
    ops = orgs.OPS()
    r = requests.get(ops.request_url)
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")
    job_table = soup.find(ops.soup_find_list[0], ops.soup_find_list[1])
    job_table = job_table.parent.table
    nums = []
    rows = job_table.find_all("a", target="_self")
    for row in rows:
        url_text = row["href"].encode('utf-8')
        url_list = url_text.split("JobID=")
        job_id = int(url_list[1])
        nums.append(job_id)
    mi = max(nums) - 100
    ma = max(nums) + 100
    return mi, ma


def crawl(mi, ma):
    results = []
    for i in range(mi, ma):
        this_url = "https://www.gojobs.gov.on.ca/Preview.aspx?JobID=" + str(i)
        page = requests.get(this_url)
        ptext = page.text
        soup = BeautifulSoup(ptext, "lxml")
        if is_posting(soup):
            results.append(this_url)
            print "found OPS OT: {}".format(this_url)
    return results


def is_posting(soup):
    pared_soup = soup.find("table", id="JobAdTable_1")
    if not pared_soup:
        return False
    if pared_soup.find_next(text="Open Targeted "):
        return True
    return False


if __name__ == '__main__':
    mi = int(sys.argv[1])
    ma = int(sys.argv[2])
    data = parse.build_ot_list(mi, ma)
    parse.update_redis(data)
