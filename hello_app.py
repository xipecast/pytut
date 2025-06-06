#!/usr/bin/env python3
import calendar

from datetime import datetime

from flask import Flask

from python_tutorial.day import dayname

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, world! Happy {dayname(datetime.now())} from a file!.</p>"
    #return "<p>hello, world!</p>"

def dayname(time):
    """Return the name of the day of the week for the given time."""
    return calendar.day_name[time.weekday()]

def greeting(time):
    """return a friendly greeting based on the current time."""
    return FILL_IN
