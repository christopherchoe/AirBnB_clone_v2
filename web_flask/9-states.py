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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id=None):
    """display state with given id
    """
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        states = storage.all(State).values()
    else:
        states = storage.all("State").values()
    if id is not None:
        found = False
        for i in states:
            states = [i]
            if id == i.id:
                break
        return render_template(
            '9-states.html', states=states, id=id)
    return render_template(
        '9-states.html', states=states)

if __name__ == '__main__':
    app.run()
