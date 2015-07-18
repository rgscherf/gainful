from flask import Flask, render_template
# from flask.ext.sqlalchemy import SQLAlchemy
from src import parse
import sys

app = Flask(__name__)

@app.route("/")
def template_test():
    data = parse.build_parse_list()
    size = str(sys.getsizeof(data))
    return render_template('template_test.html', data=data, size=size)

if __name__ == '__main__':
    app.run()

## https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
## https://realpython.com/blog/python/flask-by-example-part-1-project-setup/
