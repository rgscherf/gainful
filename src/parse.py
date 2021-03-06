from bs4 import BeautifulSoup
from itertools import chain
import requests, os, sys
import orgs
import crawl_ops_open as crawl

import redis

reload(sys)
sys.setdefaultencoding('utf8')

url = os.getenv("REDISTOGO_URL", "redis://localhost:6379")
rserver = redis.from_url(url)

organizations = [ orgs.Toronto()
         , orgs.Hamilton()
         , orgs.Mississauga()
         , orgs.CRD()
         # , orgs.OPS()
         , orgs.BCPS()
         , orgs.CivicInfo()
         , orgs.CivicInfo_North_Central()
         , orgs.CivicInfo_Lower_Mainland()
         , orgs.AMCTO()
         ]

# SINGLE INSTANCE FOR DEBUGGING:
# organizations = [ orgs.CivicInfo_North_Central() ]


def parse(org):
    try:
        r = requests.get(org.request_url)
    except requests.exceptions.SSLError:
        print "Invalid SSL cert (probably OPS is being a butt):"
        r = requests.get(org.request_url, verify=False)
    rtext = r.text
    soup = BeautifulSoup(rtext, "lxml")
    data = org.make_data(soup)
    return data


def build_parse_list():
    source = []
    for o in organizations:
        source.append(parse(o))
        print "Parsed {}".format(o.name)
    flattened_list = list(chain.from_iterable(source))

    return flattened_list


def build_ot_list(mi_explicit=None, ma_explicit=None):
    if not mi_explicit:
        print "Crawling OT with dynamic bounds..."
        mi, ma = crawl.determine_bounds()
        urls = crawl.crawl(mi, ma)
    else:
        print "Crawling OT with bounds: {}-{}".format(mi_explicit, ma_explicit)
        urls = crawl.crawl(mi_explicit, ma_explicit)
    ops = orgs.OPS()

    source = []
    for url in urls:
        source.append(ops.make_data_open_targeted(url))
    return source


def update_redis(jobs):
    no_new_jobs = True
    for job in jobs:
        if rserver.hlen(job.key) == 0:
            if no_new_jobs:
                no_new_jobs = False
            rserver.hmset(job.key, { "org": job.org
                                   , "title": job.title
                                   , "div": job.div
                                   , "date": job.date
                                   , "url": job.url
                                   , "tags": job.tags
                                   })
            print "made new redis key: {}".format(job.key)
    if no_new_jobs:
        print "No new job postings :("


def update(parse_ot=True):
    print "=================="
    print "RUNNING DB UPDATES"
    print "=================="

    print "=== Parsing job sources ==="
    base_data = build_parse_list()

    if parse_ot:
        print "=== Parsing OPS open targeted jobs ==="
        open_targeted = build_ot_list()
        data = base_data + open_targeted
    else:
        data = base_data

    print "=== Updating redis ==="
    update_redis(data)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        "Parsing job boards, excluding OPS open targeted."
        update(parse_ot=False)
    else:
        # "Parsing job boards, including OPS open targeted."
        # update(parse_ot=True)
        update(parse_ot=False)
