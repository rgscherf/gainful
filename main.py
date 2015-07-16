from flask import Flask, render_template, url_for
from flask_table import Table, Col, LinkCol
import parse

app = Flask(__name__)

class Item(object):
    def __init__(self, organization, job, division, date, url):
        self.organization = organization
        self.job = job
        self.division = division
        self.date = date
        self.url = url


class ItemTable(Table):
    organization = Col("Organization")
    # job = Col("Job")
    job = LinkCol("Job", 'joblink', url_kwargs=dict(url='url', _external='True'), attr='job')
    division = Col("Ministry/Division")
    date = Col("Date Posted")
    url = Col("URL")


def package(data):
    packaged_data = []
    for row in data:
        packaged_item = Item(row[0],row[1],row[2],row[3],row[4])
        packaged_data.append(packaged_item)

    return packaged_data

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvv

def get():
    data = parse.build_parse_list()
    packaged = package(data)

    table = ItemTable(packaged)
    return table

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

@app.route("/joblink/<url>")
def joblink(url):
    print url_for(url, _external=True)

@app.route("/")
def template_test():
    table = get()
    linkzz = url_for('http://www.google.com', _external=True)
    return render_template('template_test.html', table=table, link=linkzz)

if __name__ == '__main__':
    app.run(debug=True)
