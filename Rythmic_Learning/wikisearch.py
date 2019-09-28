# Wikipedia Seaching Tool
# Ohm Shah, Jared Fellows, Matt Skeins, Jacob Lebowitz
# Created: 09/27/2019
# Updated: 09/27/2019

import wikipedia
import sys
import os

p = wikipedia.search("Ohm")
print(p)

def searchWiki(query):
    text = wikipedia.search(query)