#!/usr/bin/python3
"""
starts Flask web app
"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """teardown for flask request
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display states list in html
    """
    return render_template('7-states_list.html', states=storage.all("State").values())

if __name__ == '__main__':
    app.run()
