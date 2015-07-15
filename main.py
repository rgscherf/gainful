from flask import Flask, render_template
import parse

app = Flask(__name__)

data = parse.build_parse_list()

@app.route("/")
def template_test():
    return render_template('template_test.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
