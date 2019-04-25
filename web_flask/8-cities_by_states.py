#!/usr/bin/python3
"""
starts Flask web app
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
import os
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """teardown for flask request
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display cities by state in html
    """
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        return render_template(
            '8-cities_by_states.html', states=storage.all(State).values())
    else:
        print('why')
        print(storage.all("State").values())
        return render_template(
            '8-cities_by_states.html', states=storage.all("State").values())

if __name__ == '__main__':
    app.run()
