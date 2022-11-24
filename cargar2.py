import pandas as pd
import aspose.words as aw
import sys
import os
import re
import nltk
import string

global url, urlRead, docText

#Input del Documento
url = input("Introduzca nombre del archivo\n") + (".txt")
docText = []
try:
    with open(url):
        contents = url.read()
except FileNotFoundError:
    msg = "El archivo " + url + " no existe"
    print(msg)

#print(docText)
