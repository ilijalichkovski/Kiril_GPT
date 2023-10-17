from lxml import etree
import html
from bs4 import BeautifulSoup
import re
import random
import numpy as np

# path of the uncompressed wikipedia XML file
transcript_path = r"C:\Users\ilija\Documents\Untitled Folder\transcripts_raw.txt"

vocab = set()

with open(transcript_path, "r", encoding="utf-8") as data:
    text = data.read()
    characters = set(text)
    vocab.update(characters)

print(vocab)

vocab_file = 'TED_vocab.txt'

with open(vocab_file, "w", encoding="utf-8") as vfile:
    for char in vocab:
        vfile.write(char + '\n')