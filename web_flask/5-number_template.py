#!/usr/bin/python3
"""
starts a Flask web application, with two different slashes
"""
from flask import Flask
from flask import render_template
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


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    display Python followed by text variable
    """
    return 'Python %s' % str(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    display n if n is an integer
    """
    try:
        return '%d is a number' % n
    except TypeError:
        pass


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """
    displays html page only if n is an integer
    """
    try:
        return render_template('5-number.html', n=str(n))
    except TypeError:
        pass

if __name__ == '__main__':
    app.run()
