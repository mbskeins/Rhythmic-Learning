import os
import requests
import operator
import re
import nltk
import json
from subprocess import *

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
from helpers.serializationHelper import *
import subprocess

import importlib.util
spec = importlib.util.spec_from_file_location("module.name", "./core/rhyme_maker.py")
ai = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ai)

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

q = Queue(connection=conn)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#@app.route("/api/generate/<wiki_term>", methods=['GET'])
#def generate(wiki_term):
@app.route("/api/generate/<text>", methods=['GET'])
def generate(text):
    out = subprocess.check_output(['python3', '/Users/augmentedmode/Desktop/All-Repos/Hackathon2019/Rhythmic_Learning/flask/core/rhyme_maker.py', text]).decode("utf-8")
    output = out.split("[Starting output]")[1].split("[Finished output]")[0].strip()
    return output.replace("'", '"')

    #result = ai.rhyme_it(text)
    #factory = RhythemPatternFactory()
    #result = factory.generate()
    # factory generate pass list of lists. return object created
    #
    '''
    delays = factory.test()
    sylabs = ['tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack', 'tack']
    results = []
    for x in range(min(len(sylabs), len(delays))):
        results.append(TtsInstance(sylabs[x], delays[x]))
        return json.dumps(results, default=to_dict)
        '''
    #return json.dumps([], default=to_dict)

if __name__ == '__main__':
    app.run()
