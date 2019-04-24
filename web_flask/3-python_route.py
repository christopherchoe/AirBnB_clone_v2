#!/usr/bin/python3
"""
starts a Flask web application, with two different slashes
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    displays Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    display C followed by text variable
    """
    return 'C %s' % str(text).replace('_', ' ')


@app.route('/python/(<text>)', strict_slashes=False)
def python_text(text='is cool')
    """
    display Python followed by text variable
    """
    return 'Python %s' % str(text).replace('_', ' ')

if __name__ == '__main__':
    app.run()
