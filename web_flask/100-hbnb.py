#!/usr/bin/python3
"""
starts Flask web app
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review
import os
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """teardown for flask request
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display html of hbnb
    """
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        states = storage.all(State).values()
        amenities = storage.all(Amenity).values()
        places = storage.all(Place).values()
    else:
        states = storage.all("State").values()
        amenities = storage.all("Amenity").values()
        places = storage.all("Place").values()
    return render_template(
        '100-hbnb.html', states=states, amenities=amenities, places=places)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
