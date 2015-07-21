from flask import Flask, render_template
# from flask.ext.sqlalchemy import SQLAlchemy
from src import parse
import sys
import operator
import redis


app = Flask(__name__)


rserver = redis.Redis("localhost")


@app.route("/")
def template_test():
    keys = rserver.keys()

    data = []
    for k in keys:
        h = rserver.hgetall(k)
        data.append(h)
    data = sorted(data, key=operator.itemgetter('date'))
    data.reverse()

    size = str(sys.getsizeof(data))
    length = str(len(keys))

    return render_template('template_test.html', data=data, size=size, length=length)


if __name__ == '__main__':
    app.run(debug=True)
