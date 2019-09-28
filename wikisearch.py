# Wikipedia Seaching Tool
# Ohm Shah, Jared Fellows, Matt Skeins, Jacob Lebowitz
# Created: 09/27/2019
# Updated: 09/27/2019

import wikipedia
import sys
import os

def searchWiki(query):
    text = wikipedia.search(query)
    return text