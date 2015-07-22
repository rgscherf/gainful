from flask import Flask, render_template
import sys
import operator
import redis
import os
import logging

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)

url = os.getenv("REDISTOGO_URL", "redis://localhost:6379")
rserver = redis.from_url(url)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route("/")
def template_test():
    keys = rserver.keys()

    data = []
    for k in keys:
        h = rserver.hgetall(k)
        data.append(h)
    data = sorted(data, key=operator.itemgetter('org', 'date'))
    data.reverse()

    size = str(sys.getsizeof(data))
    length = str(len(keys))

    return render_template('template_test.html', data=data, size=size, length=length)


if __name__ == '__main__':
    app.run(debug=True)
