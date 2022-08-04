import configparser
import os

from flask import Flask, request, render_template

configuration = configparser.ConfigParser()
configuration.read(os.path.abspath("config.ini"))

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('now') == 'NOW':
            os.system('sudo etherwake {}'.format(configuration['CONSTANTS']['hwaddr']))
        else:
            pass  # unknown
    elif request.method == 'GET':
        return render_template('index.html')

    return render_template("index.html")


if __name__ == '__main__':
    app.run()
