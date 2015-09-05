from flask import Flask, render_template
import dateutil.parser as dp
import sys
import operator
import redis
import os
import logging

import src.orgs as orgs
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)


###########
# CONSTANTS
###########
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

WEEKS_DELTA_FILTER = 3

url = os.getenv("REDISTOGO_URL", "redis://localhost:6379")
rserver = redis.from_url(url)


##################
# HELPER FUNCTIONS
##################

def build_data_by_tag(tag):
    keys = rserver.keys()
    data = []
    for k in keys:
        h = rserver.hgetall(k)
        if tag in h["tags"] and filter_by_date(h["date"]):
            data.append(h)
    data = sorted(data, key=operator.itemgetter('org', 'date'), reverse=True)
    return data

def filter_by_date(date_str):
    job_date = dp.parse(date_str).date()
    filter_cutoff = datetime.date.today() - datetime.timedelta(weeks=WEEKS_DELTA_FILTER)
    if filter_cutoff >= job_date:
        return False
    return True

#########
# ROUTING
#########

@app.route("/")
def index():
    return render_template("index.html", highlight="index")

@app.route("/new")
def jobs_new():
    today = orgs.parse_date_object(datetime.date.today())
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = orgs.parse_date_object(yesterday)

    keys = rserver.keys()
    data = []
    for k in keys:
        h = rserver.hgetall(k)
        if h["date"] == today or h["date"] == yesterday:
            data.append(h)
    data = sorted(data, key=operator.itemgetter('date'), reverse=True)
    return render_template('jobtable.html', data=data, highlight="new")


@app.route("/bc")
def jobs_bc():
    data = build_data_by_tag("bc")
    return render_template('jobtable.html', data=data, highlight="bc")


@app.route("/ontario")
def jobs_ontario():
    data = build_data_by_tag("ontario")
    return render_template('jobtable.html', data=data, highlight="ontario")


@app.route("/all")
def jobs_all():
    keys = rserver.keys()

    data = []
    for k in keys:
        h = rserver.hgetall(k)
        if filter_by_date(h["date"]):
            data.append(h)
    data = sorted(data, key=operator.itemgetter('org', 'date'), reverse=True)
    return render_template('jobtable.html', data=data, highlight="all")


@app.route("/ot")
def jobs_ops_ot():
    data = build_data_by_tag("open_targeted")
    return render_template('jobtable.html', data=data, highlight="ot")


@app.route("/about")
def about():
    return render_template("about.html", highlight="about")


######
# MAIN
######

if __name__ == '__main__':
    app.run(debug=True)
