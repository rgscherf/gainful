from flask import Flask, render_template
import sys
import operator
import redis
import os

app = Flask(__name__)

# r_url = os.environ['REDIS_URL']
# rserver = redis.Redis(r_url)
# rserver = redis.Redis("redis://h:pap3shmob8jvb126nmbvaojr44d@ec2-54-83-33-255.compute-1.amazonaws.com:11019")


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
    url = os.getenv("REDISTOGO_URL", "redis://localhost:6379")
    rserver = redis.from_url(url)
    app.run()
