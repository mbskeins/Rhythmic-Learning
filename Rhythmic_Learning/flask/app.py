import os
import requests
import operator
import re
import nltk
import json
from rq import Queue
from rq.job import Job
from worker import conn
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

q = Queue(connection=conn)

from models import *

class RhythemPatternGenerator():
    def __init__(self):
        self.quarterNote = .5
        self.halfNote = 1
        self.quarterTripletNote = .75
    
    def test(self):
        results = []
        for x in range(10):
            results.append(self.quarterNote)
            results.append(self.quarterNote)
            results.append(self.quarterNote)
            results.append(self.quarterNote)
            results.append(self.quarterTripletNote)
            results.append(self.quarterTripletNote)
            results.append(self.quarterTripletNote)
            results.append(self.halfNote)
        return results

class TtsInstance():
    def __init__(self, text, delay):
        self.text = text
        self.delay = delay

def to_dict(obj):
    return obj.__dict__

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#@app.route("/api/generate/<wiki_term>", methods=['GET'])
#def generate(wiki_term):
@app.route("/api/generate/", methods=['GET'])
def generate():
    generator = RhythemPatternGenerator()
    delays = generator.test()
    sylabs = ['The s', 'heeps in the ', 'me', 'a', 'dow, the ', 'cows in the ', 'corn. re', 'fres', 'h e', 'dit ', 'de', 'le', 'te sour', 'ce rap', 'ge', 'ni', 'us T', 'ha', 't ', 'mil', 'ke', 'd the ', 'cow wit', 'h the ', 'crum', 'ple', 'd hor', 'n, Old ', 'Brind', 'le has ', 'go', 'ne to the neigh', 'bors ', 'Cold chic', 'ken a', 'plen', 'ty', ' ', 'for a ', 'me', 'al']
    results = []
    for x in range(min(len(sylabs), len(delays))):
        results.append(TtsInstance(sylabs[x], delays[x]))
    return json.dumps(results, default=to_dict)

if __name__ == '__main__':
    app.run()