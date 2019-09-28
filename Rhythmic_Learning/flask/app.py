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
from factories.RhythemPatternFactory import RhythemPatternFactory
from models.TtsInstance import TtsInstance

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

q = Queue(connection=conn)

def to_dict(obj):
    return obj.__dict__

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#@app.route("/api/generate/<wiki_term>", methods=['GET'])
#def generate(wiki_term):
@app.route("/api/generate/", methods=['GET'])
def generate():
    factory = RhythemPatternFactory()
    delays = factory.test()
    sylabs = ['The s', 'heeps in the ', 'me', 'a', 'dow, the ', 'cows in the ', 'corn. re', 'fres', 'h e', 'dit ', 'de', 'le', 'te sour', 'ce rap', 'ge', 'ni', 'us T', 'ha', 't ', 'mil', 'ke', 'd the ', 'cow wit', 'h the ', 'crum', 'ple', 'd hor', 'n, Old ', 'Brind', 'le has ', 'go', 'ne to the neigh', 'bors ', 'Cold chic', 'ken a', 'plen', 'ty', ' ', 'for a ', 'me', 'al']
    results = []
    for x in range(min(len(sylabs), len(delays))):
        results.append(TtsInstance(sylabs[x], delays[x]))
    return json.dumps(results, default=to_dict)

if __name__ == '__main__':
    app.run()