from bs4 import BeautifulSoup
from itertools import chain
import requests
import orgs
import os
import urlparse

import redis

url = os.getenv("REDISTOGO_URL", "redis://localhost:6379")
rserver = redis.from_url(url)

# r_url = os.environ['REDIS_URL']
# rserver = redis.Redis(r_url)

# rserver = redis.Redis("redis://h:pap3shmob8jvb126nmbvaojr44d@ec2-54-83-33-255.compute-1.amazonaws.com:11019")


#removed (covered by civicinfo...)
#          , orgs.Victoria()

organizations = [ orgs.Toronto()
         , orgs.Hamilton()
         , orgs.Mississauga()
         , orgs.CRD()
         , orgs.OPS()
         , orgs.BCPS()
         , orgs.CivicInfo()
         , orgs.AMCTO()
         ]

# organizations = [ orgs.AMCTO() ]


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
        print "Parsed {}".format(o.name)
    flattened_list = list(chain.from_iterable(source))

    return flattened_list


def update_redis(jobs):
    for job in jobs:
        if rserver.hlen(job.key) == 0:
            rserver.hmset(job.key, { "org": job.org
                                   , "title": job.title
                                   , "div": job.div
                                   , "date": job.date
                                   , "url": job.url
                                   })
            print "made new redis key: {}".format(job.key)

def update():
    print "Updating redis DB:"
    data = build_parse_list()
    update_redis(data)


if __name__ == '__main__':
    update()
